import asyncio
import time
from typing import Any

import httpx

from astrbot.api import AstrBotConfig, logger
from astrbot.api.event import AstrMessageEvent, MessageChain, filter
from astrbot.api.star import Context, Star, register


@register(
    "astrbot_plugin_blue_archive_helper", "binbin", "BA活动查询与结束提醒", "1.0.2"
)
class BlueArchiveHelper(Star):
    SCHEDULE_CHECK_SECONDS = 30
    ACTIVITY_KIND_LABELS = {
        14: "活动",
        15: "总力战大决战",
        16: "多倍活动",
        17: "爬塔",
        18: "指引任务",
        19: "战术测试",
        31: "其他",
    }
    ACTIVITY_KIND_ORDER = [16, 14, 15, 17, 19, 18, 31]
    ACTIVITY_KIND_NAME_TO_ID = {v: k for k, v in ACTIVITY_KIND_LABELS.items()}
    API_URL = "https://www.gamekee.com/v1/activity/page-list"
    API_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.gamekee.com/ba/huodong/16",
        "Game-Alias": "ba",
    }
    API_PARAMS = {
        "importance": 0,
        "sort": -1,
        "keyword": "",
        "limit": 999,
        "page_no": 1,
        "serverId": 16,
        "status": 0,
    }
    def __init__(self, context: Context, config: AstrBotConfig | None = None):
        super().__init__(context)
        self.ctx: Context = context
        self.config = config or {}
        self.api_timeout_seconds = max(
            3.0, float(self.config.get("api_timeout_seconds", 10.0))
        )
        self.upcoming_window_seconds = (
            max(1, int(self.config.get("upcoming_window_hours", 24))) * 3600
        )
        self.daily_reminder_time_1 = str(
            self.config.get("daily_reminder_time_1", "03:55")
        ).strip()
        self.daily_reminder_time_2 = str(
            self.config.get("daily_reminder_time_2", "13:55")
        ).strip()
        self.daily_reminder_window_seconds = (
            max(1, int(self.config.get("daily_reminder_window_minutes", 8))) * 60
        )
        self.reminder_activity_kind_ids = self._normalize_activity_kind_ids(
            self.config.get(
                "reminder_activity_kind_names",
                [
                    self.ACTIVITY_KIND_LABELS[x]
                    for x in self.ACTIVITY_KIND_ORDER
                    if x in self.ACTIVITY_KIND_LABELS
                ],
            )
        )
        if (
            "reminder_activity_kind_names" not in self.config
            and "reminder_activity_kind_ids" in self.config
        ):
            legacy_kind_ids = self._normalize_activity_kind_ids(
                self.config.get("reminder_activity_kind_ids", [])
            )
            if legacy_kind_ids:
                self.reminder_activity_kind_ids = legacy_kind_ids
        self.default_remind_minutes = max(
            1, int(self.config.get("default_remind_minutes", 360))
        )
        self.max_remind_minutes = max(
            self.default_remind_minutes,
            int(self.config.get("max_remind_minutes", 1440)),
        )
        self.enable_persona_polish = self._to_bool(
            self.config.get("enable_persona_polish", False)
        )
        self.persona_polish_model = str(
            self.config.get("persona_polish_model", "")
        ).strip()
        self.whitelist_sessions = self._normalize_sid_list(
            self.config.get("whitelist_sessions", [])
        )
        self.blacklist_sessions = self._normalize_sid_list(
            self.config.get("blacklist_sessions", [])
        )
        self._reminder_task: asyncio.Task | None = None
        self._storage_lock: asyncio.Lock = asyncio.Lock()
        self._activity_cache: dict[str, tuple[float, list[dict[str, Any]]]] = {}
        self._CACHE_TTL_SECONDS = 300
        self._MAX_CACHE_ENTRIES = 10

    async def initialize(self):
        if self._reminder_task is None or self._reminder_task.done():
            self._reminder_task = asyncio.create_task(self._reminder_loop())

    async def terminate(self):
        if self._reminder_task and not self._reminder_task.done():
            self._reminder_task.cancel()
            try:
                await self._reminder_task
            except asyncio.CancelledError:
                pass
        self._reminder_task = None

    @staticmethod
    def _normalize_ts(value: Any) -> int | None:
        if value is None:
            return None
        try:
            ts = int(float(value))
        except (TypeError, ValueError):
            return None
        if ts > 10**12:
            ts = ts // 1000
        if ts <= 0:
            return None
        return ts

    @staticmethod
    def _fmt_ts(ts: int | None) -> str:
        if not ts:
            return "-"
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))

    @staticmethod
    def _normalize_sid_list(raw: Any) -> set[str]:
        if isinstance(raw, str):
            parts = [x.strip() for x in raw.split(",") if x.strip()]
            return set(parts)
        if isinstance(raw, list):
            return {str(x).strip() for x in raw if str(x).strip()}
        return set()

    @staticmethod
    def _to_bool(raw: Any) -> bool:
        if isinstance(raw, bool):
            return raw
        if isinstance(raw, (int, float)):
            return raw != 0
        if isinstance(raw, str):
            return raw.strip().lower() in {"1", "true", "yes", "on"}
        return False

    @classmethod
    def _normalize_activity_kind_id(cls, raw: Any) -> int | None:
        if raw is None:
            return None
        try:
            kind_id = int(float(raw))
        except (TypeError, ValueError):
            return None
        if kind_id == 0:
            return 31
        if kind_id in cls.ACTIVITY_KIND_LABELS:
            return kind_id
        return None

    @classmethod
    def _normalize_activity_kind_name(cls, raw: Any) -> int | None:
        name = str(raw or "").strip()
        if not name:
            return None
        if name in cls.ACTIVITY_KIND_NAME_TO_ID:
            return cls.ACTIVITY_KIND_NAME_TO_ID[name]
        return None

    @classmethod
    def _normalize_activity_kind_ids(cls, raw: Any) -> set[int]:
        if isinstance(raw, str):
            parts = [x.strip() for x in raw.split(",") if x.strip()]
        elif isinstance(raw, list):
            parts = raw
        else:
            parts = []
        kind_ids: set[int] = set()
        for part in parts:
            kind_id = cls._normalize_activity_kind_name(part)
            if kind_id is None:
                kind_id = cls._normalize_activity_kind_id(part)
            if kind_id is not None:
                kind_ids.add(kind_id)
        return kind_ids

    def _clean_expired_cache(self) -> None:
        now = time.time()
        expired_keys = [
            k for k, (ts, _) in self._activity_cache.items()
            if now - ts > self._CACHE_TTL_SECONDS
        ]
        for k in expired_keys:
            del self._activity_cache[k]
        if len(self._activity_cache) > self._MAX_CACHE_ENTRIES:
            sorted_keys = sorted(
                self._activity_cache.keys(),
                key=lambda k: self._activity_cache[k][0]
            )
            for k in sorted_keys[:len(self._activity_cache) - self._MAX_CACHE_ENTRIES]:
                del self._activity_cache[k]

    @classmethod
    def _resolve_activity_kind_id(cls, item: dict[str, Any]) -> int:
        kind_id = cls._normalize_activity_kind_id(item.get("activity_kind_id"))
        if kind_id is not None:
            return kind_id
        kind_name = str(item.get("activity_kind_name") or "").strip()
        if not kind_name:
            return 31
        for k, name in cls.ACTIVITY_KIND_LABELS.items():
            if name == kind_name:
                return k
        return 31

    @classmethod
    def _format_kind_labels(cls, kind_ids: set[int]) -> str:
        if not kind_ids:
            return "全部"
        ordered = [x for x in cls.ACTIVITY_KIND_ORDER if x in kind_ids]
        extras = sorted(kind_ids - set(ordered))
        labels = [cls.ACTIVITY_KIND_LABELS.get(x, str(x)) for x in ordered + extras]
        return " / ".join(labels)

    @staticmethod
    def _parse_daily_time(text: str) -> tuple[int, int] | None:
        raw = str(text).strip()
        if not raw:
            return None
        parts = raw.split(":")
        if len(parts) != 2:
            return None
        try:
            hour = int(parts[0])
            minute = int(parts[1])
        except ValueError:
            return None
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            return None
        return hour, minute

    def _get_schedule_slots(self) -> list[tuple[str, int]]:
        slots: list[tuple[str, int]] = []
        seen: set[str] = set()
        for raw in [self.daily_reminder_time_1, self.daily_reminder_time_2]:
            parsed = self._parse_daily_time(raw)
            if not parsed:
                continue
            hour, minute = parsed
            slot_text = f"{hour:02d}:{minute:02d}"
            if slot_text in seen:
                continue
            seen.add(slot_text)
            slots.append((slot_text, hour * 3600 + minute * 60))
        return slots

    async def _get_due_schedule_slot_key(self) -> str | None:
        slots = self._get_schedule_slots()
        if not slots:
            return None
        now_ts = int(time.time())
        local_now = time.localtime(now_ts)
        day_prefix = time.strftime("%Y%m%d", local_now)
        day_seconds = (
            local_now.tm_hour * 3600 + local_now.tm_min * 60 + local_now.tm_sec
        )
        due_slot_key = ""
        for slot_text, slot_seconds in slots:
            passed = day_seconds - slot_seconds
            if 0 <= passed < self.daily_reminder_window_seconds:
                due_slot_key = f"{day_prefix}@{slot_text}"
                break
        if not due_slot_key:
            return None
        raw = await self.get_kv_data("schedule_triggered_slots", {})
        triggered_slots = raw if isinstance(raw, dict) else {}
        if due_slot_key in triggered_slots:
            return None
        return due_slot_key

    async def _mark_schedule_slot_triggered(self, slot_key: str) -> None:
        now_ts = int(time.time())
        raw = await self.get_kv_data("schedule_triggered_slots", {})
        triggered_slots = raw if isinstance(raw, dict) else {}
        clean_slots = {
            str(k): int(v)
            for k, v in triggered_slots.items()
            if isinstance(k, str)
            and isinstance(v, (int, float, str))
            and now_ts - int(float(v)) < 7 * 86400
        }
        clean_slots[slot_key] = now_ts
        await self.put_kv_data("schedule_triggered_slots", clean_slots)

    def _is_allowed_umo(self, umo: str) -> bool:
        if self.whitelist_sessions and umo not in self.whitelist_sessions:
            return False
        if self.blacklist_sessions and umo in self.blacklist_sessions:
            return False
        return True

    async def _resolve_persona_prompt(self, umo: str, platform_name: str) -> str:
        try:
            provider_settings = self.ctx.get_config(umo=umo).get("provider_settings", {})
            _, persona, _, _ = await self.ctx.persona_manager.resolve_selected_persona(
                umo=umo,
                conversation_persona_id=None,
                platform_name=platform_name,
                provider_settings=provider_settings,
            )
            if isinstance(persona, dict):
                prompt = str(persona.get("prompt") or "").strip()
                if prompt:
                    return prompt
            default_persona = await self.ctx.persona_manager.get_default_persona_v3(umo)
            if isinstance(default_persona, dict):
                return str(default_persona.get("prompt") or "").strip()
        except Exception as e:
            logger.warning(f"BA人格解析失败，将回退原始文本: {e}")
        return ""

    async def _polish_text(
        self, text: str, umo: str, platform_name: str | None = None
    ) -> str:
        if not self.enable_persona_polish:
            return text
        prov = self.ctx.get_using_provider(umo=umo)
        if not prov:
            logger.warning("BA润色失败，未找到当前会话可用模型，已回退原始文本")
            return text
        resolved_platform_name = (
            platform_name or (umo.split(":", 1)[0] if ":" in umo else "")
        )
        persona_prompt = await self._resolve_persona_prompt(
            umo=umo,
            platform_name=resolved_platform_name,
        )
        system_prompt = (
            "你是一个消息润色助手。你必须基于给定人格风格润色文本，但不得改变活动名称、时间、数量和命令关键词。"
            "输出只允许是润色后的最终文本，不要额外解释。"
        )
        if persona_prompt:
            system_prompt += f"\n\n当前人格设定：\n{persona_prompt}"
        prompt = (
            "请润色下面这段将要发送给用户的文本，保持事实和格式结构，不要添加不存在的信息：\n\n"
            f"{text}"
        )
        kwargs: dict[str, Any] = {}
        if self.persona_polish_model:
            kwargs["model"] = self.persona_polish_model
        try:
            resp = await prov.text_chat(
                prompt=prompt,
                system_prompt=system_prompt,
                **kwargs,
            )
            polished = (resp.completion_text or "").strip()
            return polished or text
        except Exception as e:
            logger.warning(f"BA润色失败，将回退原始文本: {e}")
            return text

    @classmethod
    def _activity_key(cls, item: dict[str, Any]) -> str:
        title = str(item.get("title") or "").strip()
        end_at = cls._normalize_ts(item.get("end_at")) or 0
        return f"{title}|{end_at}"

    async def _fetch_activities(self) -> list[dict[str, Any]]:
        cache_key = "activities"
        now = time.time()
        cached = self._activity_cache.get(cache_key)
        if cached:
            ts, data = cached
            if now - ts <= self._CACHE_TTL_SECONDS:
                logger.debug("使用缓存的活动数据")
                return data
        for i in range(2):
            try:
                async with httpx.AsyncClient(timeout=self.api_timeout_seconds) as client:
                    resp = await client.get(
                        self.API_URL,
                        params=self.API_PARAMS,
                        headers=self.API_HEADERS,
                    )
                if resp.status_code != 200:
                    logger.warning(f"BA活动接口状态码异常: {resp.status_code}")
                    continue
                payload = resp.json()
                if payload.get("code") != 0:
                    logger.warning(f"BA活动接口业务状态异常: {payload}")
                    continue
                data = payload.get("data")
                if isinstance(data, list):
                    self._activity_cache[cache_key] = (now, data)
                    self._clean_expired_cache()
                    return data
            except Exception as e:
                logger.warning(f"BA活动接口请求失败({i + 1}/2): {e}")
                await asyncio.sleep(1)
        return []

    def _split_activities(
        self,
        activities: list[dict[str, Any]],
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        now_ts = int(time.time())
        ongoing: list[dict[str, Any]] = []
        upcoming: list[dict[str, Any]] = []
        end_ts = now_ts + self.upcoming_window_seconds
        for item in activities:
            begin_at = self._normalize_ts(item.get("begin_at"))
            finish_at = self._normalize_ts(item.get("end_at"))
            if not begin_at or not finish_at:
                continue
            if begin_at <= now_ts < finish_at:
                ongoing.append(item)
            elif now_ts < begin_at <= end_ts:
                upcoming.append(item)
        ongoing.sort(
            key=lambda x: self._normalize_ts(x.get("end_at")) or 0,
        )
        upcoming.sort(
            key=lambda x: self._normalize_ts(x.get("begin_at")) or 0,
        )
        return ongoing, upcoming

    def _build_ongoing_text(self, ongoing: list[dict[str, Any]]) -> str:
        lines: list[str] = []
        now_text = self._fmt_ts(int(time.time()))
        lines.append(f"BA进行中活动（{now_text}）")
        if not ongoing:
            lines.append("当前没有进行中的活动。")
            return "\n".join(lines)
        lines.append("")
        lines.append(f"进行中活动（{len(ongoing)}）")
        for item in ongoing:
            lines.append(
                f"- {item.get('title') or '未命名活动'} | 结束: {self._fmt_ts(self._normalize_ts(item.get('end_at')))}"
            )
        return "\n".join(lines)

    def _build_upcoming_text(self, upcoming: list[dict[str, Any]]) -> str:
        lines: list[str] = []
        now_text = self._fmt_ts(int(time.time()))
        lines.append(f"BA即将开始活动（{now_text}）")
        if not upcoming:
            lines.append("当前没有即将开始（配置窗口内）的活动。")
            return "\n".join(lines)
        lines.append("")
        lines.append(
            f"即将开始（{max(1, self.upcoming_window_seconds // 3600)}小时内）（{len(upcoming)}）"
        )
        for item in upcoming:
            lines.append(
                f"- {item.get('title') or '未命名活动'} | 开始: {self._fmt_ts(self._normalize_ts(item.get('begin_at')))}"
            )
        return "\n".join(lines)

    async def _query_split_activity_text(self) -> tuple[str, str]:
        activities = await self._fetch_activities()
        if not activities:
            fail = "活动数据获取失败，请稍后重试。"
            return fail, fail
        ongoing, upcoming = self._split_activities(activities)
        return self._build_ongoing_text(ongoing), self._build_upcoming_text(upcoming)

    async def _get_subscriptions(self) -> dict[str, dict[str, Any]]:
        async with self._storage_lock:
            raw = await self.get_kv_data("subscriptions", {})
            if isinstance(raw, dict):
                return raw
            return {}

    async def _save_subscriptions(
        self, subscriptions: dict[str, dict[str, Any]]
    ) -> None:
        async with self._storage_lock:
            await self.put_kv_data("subscriptions", subscriptions)

    async def _get_sent_reminders(self) -> dict[str, int]:
        async with self._storage_lock:
            raw = await self.get_kv_data("sent_reminders", {})
            if isinstance(raw, dict):
                return {
                    str(k): int(v)
                    for k, v in raw.items()
                    if isinstance(k, str) and isinstance(v, (int, float, str))
                }
            return {}

    async def _save_sent_reminders(self, sent: dict[str, int]) -> None:
        async with self._storage_lock:
            await self.put_kv_data("sent_reminders", sent)

    def _build_reminder_text(
        self,
        remind_minutes: int,
        activities: list[dict[str, Any]],
    ) -> str:
        lines = [f"BA活动结束提醒（{remind_minutes}分钟内）"]
        for item in activities:
            lines.append(
                f"- {item.get('title') or '未命名活动'} | 结束时间: {self._fmt_ts(self._normalize_ts(item.get('end_at')))}"
            )
        return "\n".join(lines)

    async def _process_reminders_once(self) -> None:
        subscriptions = await self._get_subscriptions()
        active_subs = {
            umo: cfg
            for umo, cfg in subscriptions.items()
            if isinstance(cfg, dict) and cfg.get("enabled", True)
        }
        if not active_subs:
            return
        activities = await self._fetch_activities()
        if not activities:
            return
        now_ts = int(time.time())
        sent = await self._get_sent_reminders()
        sent_changed = False
        for umo, cfg in active_subs.items():
            if not self._is_allowed_umo(umo):
                continue
            minutes = cfg.get("minutes", self.default_remind_minutes)
            try:
                remind_minutes = max(1, min(self.max_remind_minutes, int(minutes)))
            except (TypeError, ValueError):
                remind_minutes = self.default_remind_minutes
            window_ts = now_ts + remind_minutes * 60
            due_items: list[dict[str, Any]] = []
            for item in activities:
                begin_at = self._normalize_ts(item.get("begin_at"))
                end_at = self._normalize_ts(item.get("end_at"))
                if not begin_at or not end_at:
                    continue
                kind_id = self._resolve_activity_kind_id(item)
                if self.reminder_activity_kind_ids and (
                    kind_id not in self.reminder_activity_kind_ids
                ):
                    continue
                if begin_at > now_ts:
                    continue
                if not (now_ts < end_at <= window_ts):
                    continue
                sent_key = f"{umo}::{self._activity_key(item)}"
                if sent.get(sent_key) == end_at:
                    continue
                due_items.append(item)
                sent[sent_key] = end_at
                sent_changed = True
            if due_items:
                text = self._build_reminder_text(remind_minutes, due_items)
                text = await self._polish_text(text, umo)
                ok = await self.ctx.send_message(umo, MessageChain().message(text))
                if not ok:
                    logger.warning(f"BA结束提醒发送失败，找不到会话平台: {umo}")
        if sent_changed:
            await self._save_sent_reminders(sent)

    async def _reminder_loop(self):
        while True:
            try:
                slot_key = await self._get_due_schedule_slot_key()
                if slot_key:
                    await self._process_reminders_once()
                    await self._mark_schedule_slot_triggered(slot_key)
                await asyncio.sleep(self.SCHEDULE_CHECK_SECONDS)
            except asyncio.CancelledError:
                raise
            except Exception as e:
                logger.error(f"BA结束提醒任务异常: {e}")
                await asyncio.sleep(self.SCHEDULE_CHECK_SECONDS)

    @filter.command("ba进行中")
    async def ba_activity_command(self, event: AstrMessageEvent):
        if not self._is_allowed_umo(event.unified_msg_origin):
            return
        ongoing_text, _ = await self._query_split_activity_text()
        ongoing_text = await self._polish_text(
            ongoing_text,
            event.unified_msg_origin,
            event.get_platform_name(),
        )
        yield event.plain_result(ongoing_text)

    @filter.command("ba即将开始")
    async def ba_upcoming_command(self, event: AstrMessageEvent):
        if not self._is_allowed_umo(event.unified_msg_origin):
            return
        _, upcoming_text = await self._query_split_activity_text()
        upcoming_text = await self._polish_text(
            upcoming_text,
            event.unified_msg_origin,
            event.get_platform_name(),
        )
        yield event.plain_result(upcoming_text)

    @filter.command("ba活动")
    async def ba_activity_help(self, event: AstrMessageEvent):
        if not self._is_allowed_umo(event.unified_msg_origin):
            return
        text = await self._polish_text(
            "活动查询请使用：/ba进行中 或 /ba即将开始",
            event.unified_msg_origin,
            event.get_platform_name(),
        )
        yield event.plain_result(text)

    @filter.event_message_type(filter.EventMessageType.GROUP_MESSAGE)
    @filter.command("ba提醒开启")
    async def ba_reminder_enable(
        self, event: AstrMessageEvent, minutes: int | None = None
    ):
        if not self._is_allowed_umo(event.unified_msg_origin):
            return
        if minutes is None:
            minutes = self.default_remind_minutes
        minutes = max(1, min(self.max_remind_minutes, minutes))
        subscriptions = await self._get_subscriptions()
        subscriptions[event.unified_msg_origin] = {
            "enabled": True,
            "minutes": minutes,
            "group_id": event.get_group_id() or "",
            "updated_at": int(time.time()),
        }
        await self._save_subscriptions(subscriptions)
        text = await self._polish_text(
            f"已开启 BA 活动结束提醒，提前 {minutes} 分钟通知。",
            event.unified_msg_origin,
            event.get_platform_name(),
        )
        yield event.plain_result(text)

    @filter.event_message_type(filter.EventMessageType.GROUP_MESSAGE)
    @filter.command("ba提醒关闭")
    async def ba_reminder_disable(self, event: AstrMessageEvent):
        if not self._is_allowed_umo(event.unified_msg_origin):
            return
        subscriptions = await self._get_subscriptions()
        if event.unified_msg_origin in subscriptions:
            subscriptions[event.unified_msg_origin]["enabled"] = False
            subscriptions[event.unified_msg_origin]["updated_at"] = int(time.time())
            await self._save_subscriptions(subscriptions)
        text = await self._polish_text(
            "已关闭 BA 活动结束提醒。",
            event.unified_msg_origin,
            event.get_platform_name(),
        )
        yield event.plain_result(text)

    @filter.event_message_type(filter.EventMessageType.GROUP_MESSAGE)
    @filter.command("ba提醒状态")
    async def ba_reminder_status(self, event: AstrMessageEvent):
        if not self._is_allowed_umo(event.unified_msg_origin):
            return
        subscriptions = await self._get_subscriptions()
        cfg = subscriptions.get(event.unified_msg_origin) or {}
        enabled = bool(cfg.get("enabled", False))
        minutes = int(cfg.get("minutes", self.default_remind_minutes))
        all_enabled = sum(
            1
            for v in subscriptions.values()
            if isinstance(v, dict) and v.get("enabled", True)
        )
        status_text = (
            f"本群提醒状态：{'开启' if enabled else '关闭'}\n"
            f"提前提醒分钟：{minutes}\n"
            f"通知活动类型：{self._format_kind_labels(self.reminder_activity_kind_ids)}\n"
            f"固定时段：{self.daily_reminder_time_1} / {self.daily_reminder_time_2}\n"
            f"固定时段窗口：{self.daily_reminder_window_seconds // 60} 分钟\n"
            f"即将开始窗口：{self.upcoming_window_seconds // 3600} 小时\n"
            f"当前启用提醒的群数量：{all_enabled}"
        )
        status_text = await self._polish_text(
            status_text,
            event.unified_msg_origin,
            event.get_platform_name(),
        )
        yield event.plain_result(status_text)

import asyncio
import time
from typing import Any

import httpx

from astrbot.api import AstrBotConfig, logger
from astrbot.api.event import AstrMessageEvent, MessageChain, filter
from astrbot.api.star import Context, Star, register


@register(
    "astrbot_plugin_blue_archive_helper", "binbin", "BA活动查询与结束提醒", "1.0.1"
)
class BlueArchiveHelper(Star):
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
        self.reminder_poll_seconds = (
            max(1, int(self.config.get("reminder_poll_minutes", 30))) * 60
        )
        self.default_remind_minutes = max(
            1, int(self.config.get("default_remind_minutes", 30))
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
        raw = await self.get_kv_data("subscriptions", {})
        if isinstance(raw, dict):
            return raw
        return {}

    async def _save_subscriptions(
        self, subscriptions: dict[str, dict[str, Any]]
    ) -> None:
        await self.put_kv_data("subscriptions", subscriptions)

    async def _get_sent_reminders(self) -> dict[str, int]:
        raw = await self.get_kv_data("sent_reminders", {})
        if isinstance(raw, dict):
            return {
                str(k): int(v)
                for k, v in raw.items()
                if isinstance(k, str) and isinstance(v, (int, float, str))
            }
        return {}

    async def _save_sent_reminders(self, sent: dict[str, int]) -> None:
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
                await self._process_reminders_once()
            except asyncio.CancelledError:
                raise
            except Exception as e:
                logger.error(f"BA结束提醒任务异常: {e}")
            await asyncio.sleep(self.reminder_poll_seconds)

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
            f"轮询周期：{self.reminder_poll_seconds // 60} 分钟\n"
            f"即将开始窗口：{self.upcoming_window_seconds // 3600} 小时\n"
            f"当前启用提醒的群数量：{all_enabled}"
        )
        status_text = await self._polish_text(
            status_text,
            event.unified_msg_origin,
            event.get_platform_name(),
        )
        yield event.plain_result(status_text)

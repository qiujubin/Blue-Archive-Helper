# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AstrBot plugin that provides Blue Archive (蔚蓝档案) activity lookup and end-of-event reminders for QQ groups.

## Commands

| Command | Description |
|---------|-------------|
| `/ba进行中` | Query currently ongoing activities |
| `/ba即将开始` | Query activities starting within the configured window |
| `/ba活动` | Show help hint |
| `/ba提醒开启 [分钟]` | Enable reminders for this group (default: 360 min) |
| `/ba提醒关闭` | Disable reminders for this group |
| `/ba提醒状态` | Show reminder status for this group |

## Key Files

- `main.py` - Single-file plugin containing the `BlueArchiveHelper` Star subclass
- `metadata.yaml` - Plugin metadata (name, version, author)
- `_conf_schema.json` - WebUI configuration schema
- `test.py` - Standalone script to test the gamekee.com API directly (run with `python test.py`)

## Architecture

**Single-Star plugin** with three logical layers:

1. **Command handlers** (bottom of `main.py`) - decorate with `@filter.command()`; each yields `event.plain_result()`
2. **Business logic** - `_query_split_activity_text()`, `_process_reminders_once()`, `_polish_text()`
3. **Data layer** - `_fetch_activities()` (HTTP, cached 5 min), KV store for subscriptions/reminders

**Reminder scheduling**: Fixed two daily slots (`daily_reminder_time_1/2`). `_reminder_loop()` wakes every 30s to check if within the window. Uses `PluginKVStoreMixin.get_kv_data`/`put_kv_data` for persistence and `asyncio.Lock` for concurrent write safety.

**Activity kind IDs**: 14=活动, 15=总力战大决战, 16=多倍活动, 17=爬塔, 18=指引任务, 19=战术测试, 31=其他. Priority order: `[16, 14, 15, 17, 19, 18, 31]`.

## Configuration

All config is via `_conf_schema.json`. Key settings:
- `default_remind_minutes` (default: 360) - used when `/ba提醒开启` is called without args
- `enable_persona_polish` (default: false) - uses the bot's current persona to polish output text
- `whitelist_sessions` / `blacklist_sessions` - control which sessions can trigger the plugin

## API

Activity data comes from `https://www.gamekee.com/v1/activity/page-list`. This is a direct dependency — if the API changes, `_fetch_activities()` and the hardcoded `API_PARAMS`/`API_HEADERS` will need updating.

## Development References

- AstrBot plugin docs: `AstrBot_Docs.md`
- AstrBot core (for Context, Star, filter decorators): upstream `astrbot` package

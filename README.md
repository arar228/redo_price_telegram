# REDO Price Tracker

A focused Python worker that fetches REDO market data from DexScreener and publishes formatted updates to a Telegram channel. It demonstrates a small integration boundary: external API data, message formatting, channel-permission checks, and a configurable polling loop.

[Source map](#source-map) · [Setup](#setup-requirements) · [Русский](docs/README.ru.md)

## Source map

| Source | Responsibility |
|---|---|
| [price_tracker.py](price_tracker.py) — `get_token_price` | Market-data retrieval |
| [price_tracker.py](price_tracker.py) — `format_price_message` | Price and timeframe formatting |
| [price_tracker.py](price_tracker.py) — `check_bot_permissions`, `send_price_update`, `run_tracker` | Telegram delivery and worker lifecycle |
| [config.py](config.py) | Environment-based settings |
| [Procfile](Procfile), [runtime.txt](runtime.txt) | Existing deployment entry point and runtime declaration |
| [setup_instructions.md](setup_instructions.md) | Existing Russian setup notes |

**Stack:** Python, asyncio, `python-telegram-bot==20.7`, and `requests==2.31.0`. Data fetching uses synchronous Requests calls inside the worker. Updates include price changes over the 5-minute, 1-hour, 6-hour, and 24-hour windows available from the provider.

## Setup requirements

```bash
git clone https://github.com/arar228/redo_price_telegram.git
cd redo_price_telegram
python -m venv .venv
# Activate .venv using your shell's activation command.
python -m pip install -r requirements.txt
```

Choose a Python runtime compatible with the pinned packages; treat `runtime.txt` as a historical deployment declaration to recheck when restoring the service.

| Environment variable | Purpose |
|---|---|
| `BOT_TOKEN` | Bot authentication |
| `CHAT_ID` | Intended channel recipient |
| `TOKEN_CA` | Tracked token contract address; this is public asset identity, not a signing key |
| `DEXSCREENER_API`, `DEXSCREENER_URL` | API and display-link configuration |
| `UPDATE_INTERVAL` | Polling interval |

The current `config.py` reads the **process environment** and does not call `load_dotenv()`. Export settings through your shell/service manager or an existing launcher; copying `.env.example` into `.env` alone does not load those settings.

After provisioning a dedicated test channel and bot permissions, the declared worker command is:

```bash
python price_tracker.py
```

This command sends real Telegram messages. External market data can be stale, incomplete, or unavailable; published figures are informational rather than guaranteed execution prices.

## Review status

Source/documentation review: **2026-09-07**. No provider calls, Telegram messages, live deployment check, or end-to-end tests were performed in this pass. No GitHub Actions workflow is included in this snapshot.

Keep credentials and channel-specific settings outside public examples. A useful next verification is a recorded DexScreener response test for formatting, followed by one controlled delivery to a test channel. Existing [Russian setup notes](setup_instructions.md) remain available; the environment-loading clarification above applies to this revision.

import os

# Конфигурация бота
# Используем переменные окружения для безопасности (Railway, Heroku и т.д.)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
CHAT_ID = os.getenv("CHAT_ID", "YOUR_CHAT_ID_HERE")
TOKEN_CA = os.getenv("TOKEN_CA", "EQBZ_cafPyDr5KUTs0aNxh0ZTDhkpEZONmLJA2SNGlLm4Cko")
DEXSCREENER_URL = os.getenv("DEXSCREENER_URL", "https://dexscreener.com/ton/eqbcwe_iobxa4mt3rbchil2s4-v4yqs3wudt1-dvzoceemgo")

# Настройки обновления
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", "60"))  # секунды (1 минута)

# API endpoints
DEXSCREENER_API = os.getenv("DEXSCREENER_API", "https://api.dexscreener.com/latest/dex/tokens/")

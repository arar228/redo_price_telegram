# REDO Price Tracker Bot 📊

*(Русская версия ниже / Russian version below)*

A professional Telegram bot designed to track the REDO token price in real-time and broadcast formatted updates to a Telegram channel. It leverages the global DexScreener API to fetch accurate token data, including price changes over multiple timeframes.

## Features ✨
- **Real-time Price Tracking:** Automatically fetches the latest REDO token price via DexScreener API.
- **Detailed Timeframes:** Displays price percentage changes for 5 minutes, 1 hour, 6 hours, and 24 hours.
- **Visual Indicators:** Uses intuitive emojis (🟢 / 🔴) to easily spot bullish or bearish trends.
- **Automated Broadcasts:** Sends updates to a designated Telegram channel every minute (configurable).
- **Environment Driven:** Securely relies on `.env` variables, making it safe for production deployments and public repositories.

## Installation & Setup 🚀

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/redo_price_telegram.git
   cd redo_price_telegram
   ```

2. **Install dependencies:**
   Make sure you have Python 3.7+ installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Environment:**
   Copy `.env.example` to `.env` and fill in your details:
   ```bash
   cp .env.example .env
   ```
   *Required variables:*
   - `BOT_TOKEN`: Your Telegram Bot token from @BotFather.
   - `CHAT_ID`: The target channel ID (e.g., `-1001234567890`) where the bot is added as an administrator.

4. **Run the Bot:**
   ```bash
   python price_tracker.py
   ```

## Deployment Platform (Railway / Heroku) ☁️

This project includes a `Procfile` and `runtime.txt`, making it ready for seamless deployment on platforms like Railway or Heroku. 
Simply connect your GitHub repository and set the required environment variables in your platform's dashboard.

---

# Бот для Отслеживания Цены REDO 📊

Профессиональный Telegram-бот для отслеживания цены токена REDO в реальном времени и отправки обновлений в Telegram-канал. Бот использует API DexScreener для получения точных данных о токене, включая изменения цены за разные периоды времени.

## Особенности ✨
- **Отслеживание в реальном времени:** Автоматически получает последнюю цену токена REDO через DexScreener API.
- **Детальная статистика:** Отображает процентное изменение цены за 5 минут, 1 час, 6 часов и 24 часа.
- **Визуальные индикаторы:** Использует интуитивно понятные эмодзи (🟢 / 🔴) для отображения тренда.
- **Автоматическая рассылка:** Отправляет обновления в указанный канал каждую минуту (настраивается).
- **Безопасная конфигурация:** Использует переменные окружения (`.env`), что делает проект безопасным для публичных репозиториев и деплоя.

## Установка и запуск 🚀

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/yourusername/redo_price_telegram.git
   cd redo_price_telegram
   ```

2. **Установите зависимости:**
   Требуется Python 3.7 или выше.
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройте окружение:**
   Скопируйте файл `.env.example` в `.env` и заполните ваши данные:
   ```bash
   cp .env.example .env
   ```
   *Необходимые переменные:*
   - `BOT_TOKEN`: Токен вашего Telegram-бота от @BotFather.
   - `CHAT_ID`: ID целевого канала (например, `-1001234567890`). **Бот должен быть администратором канала**.

4. **Запустите бота:**
   ```bash
   python price_tracker.py
   ```

## Деплой (Railway / Heroku) ☁️

Проект включает `Procfile` и `runtime.txt`, что делает его полностью готовым к быстрому развертыванию на облачных платформах (Railway, Heroku и др.). Подключите ваш GitHub репозиторий и укажите переменные окружения в панели управления хостинга.

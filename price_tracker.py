import requests
import json
import time
from datetime import datetime, timedelta
from config import BOT_TOKEN, CHAT_ID, TOKEN_CA, DEXSCREENER_API, UPDATE_INTERVAL
import asyncio
from telegram import Bot
from telegram.error import TelegramError

class RedoPriceTracker:
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)
        self.chat_id = CHAT_ID
        self.token_ca = TOKEN_CA
        self.api_url = DEXSCREENER_API
        
    async def get_token_price(self):
        """Получает цену токена REDO через DexScreener API"""
        try:
            url = f"{self.api_url}{self.token_ca}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if 'pairs' in data and len(data['pairs']) > 0:
                # Ищем пару с наибольшей ликвидностью
                best_pair = None
                max_liquidity = 0
                
                for pair in data['pairs']:
                    liquidity_usd = float(pair.get('liquidity', {}).get('usd', 0))
                    if liquidity_usd > max_liquidity:
                        max_liquidity = liquidity_usd
                        best_pair = pair
                
                if not best_pair:
                    best_pair = data['pairs'][0]
                
                price_usd = float(best_pair.get('priceUsd', 0))
                
                # Получаем все данные изменений из API DexScreener
                price_changes = best_pair.get('priceChange', {})
                price_change_5min = float(price_changes.get('m5', 0))  # 5 минут
                price_change_1h = float(price_changes.get('h1', 0))    # 1 час
                price_change_6h = float(price_changes.get('h6', 0))    # 6 часов
                price_change_24h = float(price_changes.get('h24', 0))  # 24 часа
                
                # Отладочная информация
                print(f"API Data - 5M: {price_change_5min}%, 1H: {price_change_1h}%, 6H: {price_change_6h}%, 24H: {price_change_24h}%")
                
                return {
                    'price': price_usd,
                    'change_24h': price_change_24h,
                    'change_5min': price_change_5min,
                    'change_1h': price_change_1h,
                    'change_6h': price_change_6h,
                    'timestamp': datetime.now(),
                    'pair_info': {
                        'dex': best_pair.get('dexId', 'Unknown'),
                        'liquidity': max_liquidity
                    }
                }
            else:
                print("No pairs found in API response")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price data: {e}")
            return None
        except (KeyError, ValueError, TypeError) as e:
            print(f"Error parsing price data: {e}")
            return None
    
    
    
    def format_price_message(self, price_data):
        """Форматирует сообщение согласно примеру из Telegram"""
        if not price_data:
            return None
            
        price = price_data['price']
        change_24h = price_data['change_24h']
        change_5min = price_data.get('change_5min', 0)
        change_1h = price_data.get('change_1h', 0)
        change_6h = price_data.get('change_6h', 0)
        
        # Форматируем цену с 4 знаками после запятой
        formatted_price = f"{price:.4f}"
        
        # Определяем эмодзи для изменения цены
        if change_24h >= 0:
            price_emoji = "🟢"
        else:
            price_emoji = "🔴"
        
        # Форматируем процентные изменения (все данные от API)
        change_5min_str = f"{change_5min:+.2f}%" if change_5min != 0 else "0.00%"
        change_1h_str = f"{change_1h:+.2f}%" if change_1h != 0 else "0.00%"
        change_6h_str = f"{change_6h:+.2f}%" if change_6h != 0 else "0.00%"
        change_24h_str = f"{change_24h:+.2f}%"
        
        # Создаем сообщение без данных за 7 дней
        message = f"{price_emoji} $REDO price {formatted_price}$ | {change_24h_str}\n"
        message += f"🕐 5M: {change_5min_str} | 1H: {change_1h_str} | 6H: {change_6h_str} | 24H: {change_24h_str}"
        
        return message
    
    async def check_bot_permissions(self):
        """Проверяет права бота в канале"""
        try:
            chat_member = await self.bot.get_chat_member(self.chat_id, (await self.bot.get_me()).id)
            return chat_member.status in ['administrator', 'creator']
        except TelegramError as e:
            print(f"Error checking bot permissions: {e}")
            return False
    
    async def send_price_update(self, message):
        """Отправляет обновление цены в Telegram канал"""
        try:
            # Проверяем права бота перед отправкой
            if not await self.check_bot_permissions():
                print("Bot doesn't have administrator rights in the channel!")
                print("Please add the bot as an administrator with 'Post Messages' permission.")
                return False
            
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode='HTML'
            )
            print(f"Price update sent successfully at {datetime.now().strftime('%H:%M:%S')}")
            return True
        except TelegramError as e:
            print(f"Error sending message: {e}")
            if "Need administrator rights" in str(e):
                print("\n" + "="*50)
                print("РЕШЕНИЕ ПРОБЛЕМЫ:")
                print("1. Откройте ваш канал 'Redo Price'")
                print("2. Перейдите в 'Управление каналом' -> 'Администраторы'")
                print("3. Добавьте бота как администратора")
                print("4. Дайте боту права 'Отправка сообщений'")
                print("5. Перезапустите бота")
                print("="*50)
            return False
    
    async def run_tracker(self):
        """Основной цикл отслеживания цены"""
        print("Starting REDO price tracker...")
        print(f"Chat ID: {self.chat_id}")
        print(f"Update interval: {UPDATE_INTERVAL} seconds")
        
        while True:
            try:
                # Получаем данные о цене
                price_data = await self.get_token_price()
                
                if price_data:
                    # Форматируем сообщение
                    message = self.format_price_message(price_data)
                    
                    if message:
                        # Отправляем в канал
                        await self.send_price_update(message)
                    else:
                        print("Failed to format price message")
                else:
                    print("Failed to get price data")
                
                # Ждем до следующего обновления
                await asyncio.sleep(UPDATE_INTERVAL)
                
            except KeyboardInterrupt:
                print("\nStopping price tracker...")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
                await asyncio.sleep(10)  # Ждем 10 секунд перед повтором

async def main():
    tracker = RedoPriceTracker()
    await tracker.run_tracker()

if __name__ == "__main__":
    asyncio.run(main())

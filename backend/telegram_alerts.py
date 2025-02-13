import telegram
import asyncio
from config import Config

class TelegramAlertService:
    def __init__(self):
        self.bot = telegram.Bot(token=Config.TELEGRAM_BOT_TOKEN)
        self.chat_id = Config.TELEGRAM_CHAT_ID

    async def send_alert(self, message):
        """Send trading alert via Telegram."""
        await self.bot.send_message(
            chat_id=self.chat_id, 
            text=message, 
            parse_mode='HTML'
        )

    def send_trading_alert(self, signals):
        """Construct and send trading alerts."""
        if signals['buy_signals']:
            message = "🟢 BUY SIGNAL DETECTED! \nConditions met for potential buying opportunity."
            asyncio.run(self.send_alert(message))
        
        if signals['sell_signals']:
            message = "🔴 SELL SIGNAL DETECTED! \nConditions met for potential selling opportunity."
            asyncio.run(self.send_alert(message))

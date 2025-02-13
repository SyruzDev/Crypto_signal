from binance.client import Client
from config import Config

class BinanceService:
    def __init__(self):
        self.client = Client(
            Config.BINANCE_API_KEY, 
            Config.BINANCE_SECRET_KEY
        )

    def get_historical_prices(self, symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR):
        """Fetch historical price data for a given symbol."""
        klines = self.client.get_klines(symbol=symbol, interval=interval)
        prices = [float(kline[4]) for kline in klines]  # Close prices
        return prices

from indicators import (
    calculate_rsi, 
    calculate_moving_averages, 
    calculate_bollinger_bands
)

class TradingSignalAnalyzer:
    def __init__(self, prices):
        self.prices = prices
        self.rsi = calculate_rsi(prices)
        self.fast_ma, self.slow_ma = calculate_moving_averages(prices)
        self.upper_bb, self.middle_bb, self.lower_bb = calculate_bollinger_bands(prices)

    def generate_signals(self):
        signals = {
            'buy_signals': self._detect_buy_signals(),
            'sell_signals': self._detect_sell_signals()
        }
        return signals

    def _detect_buy_signals(self):
        buy_conditions = (
            (self.rsi < 30) &  # Oversold condition
            (self.fast_ma > self.slow_ma) &  # Bullish moving average crossover
            (self.prices <= self.lower_bb)  # Price touches lower Bollinger Band
        )
        return buy_conditions

    def _detect_sell_signals(self):
        sell_conditions = (
            (self.rsi > 70) &  # Overbought condition
            (self.fast_ma < self.slow_ma) &  # Bearish moving average crossover
            (self.prices >= self.upper_bb)  # Price touches upper Bollinger Band
        )
        return sell_conditions

import numpy as np
import pandas as pd
import talib

def calculate_rsi(prices, period=14):
    """Calculate RSI for given price series."""
    return talib.RSI(prices, timeperiod=period)

def calculate_moving_averages(prices, fast_period=10, slow_period=30):
    """Calculate fast and slow moving averages."""
    fast_ma = talib.SMA(prices, timeperiod=fast_period)
    slow_ma = talib.SMA(prices, timeperiod=slow_period)
    return fast_ma, slow_ma

def calculate_macd(prices, fast_period=12, slow_period=26, signal_period=9):
    """Calculate MACD indicators."""
    macd, signal, _ = talib.MACD(
        prices, 
        fastperiod=fast_period, 
        slowperiod=slow_period, 
        signalperiod=signal_period
    )
    return macd, signal

def calculate_bollinger_bands(prices, period=20, stddev=2):
    """Calculate Bollinger Bands."""
    upper, middle, lower = talib.BBANDS(
        prices, 
        timeperiod=period, 
        nbdevup=stddev, 
        nbdevdn=stddev, 
        matype=0
    )
    return upper, middle, lower

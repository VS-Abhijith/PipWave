# ema.py

import pandas as pd

def calculate_ema(data, window=14):
    return data['Close'].ewm(span=window, adjust=False).mean()

def detect_ema_trend(data):
    data['EMA14'] = calculate_ema(data)
    data['EMA_Trend'] = np.where(data['Close'] > data['EMA14'], 'Uptrend', 'Downtrend')
    return data

# msnr.py

import pandas as pd
import numpy as np

def detect_market_structure(data):
    # Your market structure logic goes here
    data['SMA14'] = data['Close'].rolling(window=14).mean()
    data['Trend'] = np.where(data['Close'] > data['SMA14'], 'Uptrend', 'Downtrend')
    data['Market_Structure'] = 'Neutral'
    
    for i in range(2, len(data)):
        if data['Close'][i] > data['Close'][i-1] and data['Close'][i-1] > data['Close'][i-2]:
            data['Market_Structure'][i] = 'Higher High'
        elif data['Close'][i] < data['Close'][i-1] and data['Close'][i-1] < data['Close'][i-2]:
            data['Market_Structure'][i] = 'Lower Low'
        elif data['Close'][i] > data['Close'][i-1]:
            data['Market_Structure'][i] = 'Higher Low'
        else:
            data['Market_Structure'][i] = 'Lower High'
    
    return data

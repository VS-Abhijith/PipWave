import pandas as pd
import numpy as np

def calculate_sma(data, window=14):
    """
    Simple Moving Average (SMA) for trend detection.
    """
    return data['Close'].rolling(window=window).mean()

def detect_market_structure(data):
    """
    Detect Market Structure: Higher Highs (HH), Higher Lows (HL), Lower Highs (LH), Lower Lows (LL).
    """
    data['SMA14'] = calculate_sma(data)
    data['Trend'] = np.where(data['Close'] > data['SMA14'], 'Uptrend', 'Downtrend')

    # Detect Higher Highs, Higher Lows, Lower Highs, Lower Lows
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

if __name__ == "__main__":
    # Example: Market Structure for JPYUSD
    data = pd.read_csv('path_to_your_data.csv')  # Replace with your downloaded forex data
    structured_data = detect_market_structure(data)
    print("Market Structure Detected:", structured_data[['Date', 'Close', 'Market_Structure']].tail())

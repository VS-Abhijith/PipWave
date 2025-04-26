import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_forex_data(pair='JPYUSD', start_date='2020-01-01', end_date=None, interval='1d'):
    """
    Fetch historical forex data from Yahoo Finance.
    Parameters:
        pair (str): Currency pair (e.g. 'JPYUSD').
        start_date (str): Start date (format 'YYYY-MM-DD').
        end_date (str): End date (format 'YYYY-MM-DD').
        interval (str): Data interval (e.g. '1d', '1h', '5m').
    Returns:
        pd.DataFrame: Forex data in a pandas DataFrame.
    """
    if end_date is None:
        # Automatically use the current date if no end date is provided
        end_date = datetime.today().strftime('%Y-%m-%d')

    data = yf.download(pair, start=start_date, end=end_date, interval=interval)
    
    # Adding a column for pair for reference
    data['Pair'] = pair
    return data

def fetch_multi_timeframe_data(pair='JPYUSD', start_date='2020-01-01'):
    """
    Fetch forex data for multiple timeframes.
    """
    timeframes = ['1d', '1h', '5m']
    data_dict = {}

    for tf in timeframes:
        data_dict[tf] = fetch_forex_data(pair, start_date, interval=tf)
    
    return data_dict

if __name__ == "__main__":
    # Fetch data for JPYUSD with auto up-to-date
    data = fetch_forex_data('JPYUSD')
    print("Fetched JPYUSD Data:", data.tail())

    # Fetch multi-timeframe data
    multi_data = fetch_multi_timeframe_data('JPYUSD')
    for timeframe, df in multi_data.items():
        print(f"Fetched {timeframe} Data:")
        print(df.tail())

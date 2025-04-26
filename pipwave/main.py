# main.py

from data_fetcher import fetch_forex_data
from msnr import detect_market_structure
from ema import detect_ema_trend
from order_blocks import detect_order_blocks
from fvg import detect_fvg
from signal_generator import generate_trading_signal

def main():
    # Fetch forex data (e.g., JPYUSD)
    data = fetch_forex_data(pair='JPYUSD')
    
    # Perform Market Structure and EMA Analysis
    data = detect_market_structure(data)
    data = detect_ema_trend(data)
    
    # Detect Order Blocks and FVG
    order_blocks = detect_order_blocks(data)
    fvg = detect_fvg(data)
    
    # Generate Trading Signals
    data = generate_trading_signal(data)
    
    # Save the data with predictions
    data.to_csv('pipwave_predictions.csv')
    
    # Output the final predictions
    print(data[['Date', 'Close', 'Market_Structure', 'EMA_Trend', 'Signal']].tail())

if __name__ == "__main__":
    main()

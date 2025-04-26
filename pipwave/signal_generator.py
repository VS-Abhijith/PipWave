# signal_generator.py

def generate_trading_signal(data):
    signal = []
    
    # Combine the analysis (MSNR, EMA, etc.) to generate signals
    for i in range(len(data)):
        if data['Market_Structure'][i] in ['Higher High', 'Higher Low'] and data['EMA_Trend'][i] == 'Uptrend':
            signal.append('Buy')
        elif data['Market_Structure'][i] in ['Lower High', 'Lower Low'] and data['EMA_Trend'][i] == 'Downtrend':
            signal.append('Sell')
        else:
            signal.append('Hold')

    data['Signal'] = signal
    return data

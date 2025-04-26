# instruments.py
# This module handles selection of forex instruments

def get_available_pairs():
    """Returns a list of supported forex pairs."""
    return ['JPYUSD', 'EURUSD', 'GBPUSD', 'AUDUSD', 'USDCHF', 'USDCAD', 'NZDUSD']

def validate_pair(pair):
    """Validates if the input pair is supported."""
    pairs = get_available_pairs()
    return pair.upper() in pairs

if __name__ == "__main__":
    print(get_available_pairs())

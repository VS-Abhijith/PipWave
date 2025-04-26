# order_blocks.py

def detect_order_blocks(data, block_size=10):
    order_blocks = []
    for i in range(block_size, len(data)):
        high_range = data['High'][i-block_size:i].max() - data['Low'][i-block_size:i].min()
        if high_range < data['Close'][i] * 0.01:  # 1% price range
            if data['Close'][i] > data['Close'][i-block_size]:
                order_blocks.append((i, 'Buy Order Block'))
            else:
                order_blocks.append((i, 'Sell Order Block'))
    
    return order_blocks

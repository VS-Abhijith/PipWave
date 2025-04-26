# fvg.py

def detect_fvg(data, gap_threshold=0.002):  # 0.2% gap
    fvg = []
    for i in range(1, len(data)):
        gap = abs(data['Close'][i] - data['Open'][i-1]) / data['Open'][i-1]
        if gap > gap_threshold:
            fvg.append((i, 'FVG Detected'))
    return fvg

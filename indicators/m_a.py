from config import SMA_WINDOW

def calculate_sma(data):
    """Calculates Simple Moving Average"""
    data[f'SMA_{SMA_WINDOW}'] = data['Close'].rolling(SMA_WINDOW).mean()
    return data
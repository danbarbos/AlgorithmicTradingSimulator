import yfinance as yf
from config import TICKER, START_DATE, END_DATE

def fetch_stock_data():
    """Downloads OHLCV data from Yahoo Finance"""
    data = yf.download(
        TICKER,
        start=START_DATE,
        end=END_DATE,
        progress=False
    )
    return data.dropna()

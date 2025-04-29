# projects

# Algorithmic Trading Simulator

![Python](https://img.shields.io/badge/python-3.8+-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/danbarbos/algorithmic-trading-simulator)
![License](https://img.shields.io/badge/license-MIT-green)

A Python-based platform for backtesting trading strategies with technical indicators.

## Features
- 📈 Fetches real market data via Yahoo Finance
- 📊 Implements SMA, RSI, and other technical indicators
- 🧪 Backtesting engine with slippage simulation
- 📉 Interactive visualization with Matplotlib

## Project Structure

```
project/
├── data/              # Market data handlers
│   └── fetcher.py
├── indicators/        # Technical indicators
│   ├── m_a.py         # Moving averages
│   └── rsi.py         # Relative Strength Index
├── visualization/     # Plotting tools
│   └── plotter.py
├── config.py          # Strategy parameters
├── main.py            # Entry point
├── requirements.txt
└── README.md
```

## Quick Start
```bash
# Clone repository
git clone https://github.com/danbarbos/algorithmic-trading-simulator.git
cd algorithmic-trading-simulator

# Install dependencies
pip install -r requirements.txt

# Run backtest
python main.py
```

## Configuration

```python
TICKER = "AAPL"        # Stock symbol
START_DATE = "2020-01-01"
END_DATE = "2023-12-31"
SMA_WINDOW = 20        # Moving average period
RSI_WINDOW = 14        # RSI lookback period
```

## Example Strategy

```python
# Simple SMA crossover strategy
if data['Close'] > data['SMA_20'] and data['RSI'] < 30:
    enter_long()
elif data['RSI'] > 70:
    exit_position()
```

## License

MIT © Dan-Alexandru Barbos




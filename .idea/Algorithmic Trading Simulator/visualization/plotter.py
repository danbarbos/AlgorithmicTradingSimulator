import matplotlib.pyplot as plt
from matplotlib import gridspec
from config import TICKER, SMA_WINDOW, RSI_WINDOW  # Critical import added

def plot_technical_analysis(data):
    """Generates professional trading charts"""
    fig = plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(3, 1, height_ratios=[3, 1, 1])

    # Price + SMA Plot
    ax1 = plt.subplot(gs[0])
    ax1.plot(data['Close'], label=f'{TICKER} Price', color='#1f77b4', linewidth=1.5)
    ax1.plot(data[f'SMA_{SMA_WINDOW}'],
             label=f'{SMA_WINDOW}-day SMA',
             color='#ff7f0e',
             linestyle='--')

    # RSI Plot
    ax2 = plt.subplot(gs[1])
    ax2.plot(data['RSI'], label=f'{RSI_WINDOW}-day RSI', color='#2ca02c')
    ax2.axhline(70, color='red', linestyle=':', alpha=0.5)
    ax2.axhline(30, color='green', linestyle=':', alpha=0.5)

    plt.tight_layout()
    plt.show()
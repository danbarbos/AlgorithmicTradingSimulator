from data.fetcher import fetch_stock_data
from indicators.m_a import calculate_sma
from indicators.rsi import calculate_rsi
from visualization.plotter import plot_technical_analysis

class TradingSystem:
    def __init__(self):
        self.data = None

    def run(self):
        """Pipeline execution"""
        try:
            # Data pipeline
            self.data = fetch_stock_data()
            self.data = calculate_sma(self.data)
            self.data = calculate_rsi(self.data)

            # Visualization
            plot_technical_analysis(self.data)

        except Exception as e:
            print(f"Error in execution: {str(e)}")

if __name__ == "__main__":
    system = TradingSystem()
    system.run()
import pandas as pd
from src.swch import swch 

class Backtester:
    def __init__(self, strategy):
        self.strategy = strategy

    def backtest(self, historical_data):
        df = pd.DataFrame(historical_data)
        
        signals = []
        for i in range(20, len(df)):  
            signal = self.strategy.generate_signal(df.iloc[:i])
            if signal:
                signals.append(signal)
        return signals
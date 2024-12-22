import pandas as pd
import numpy as np

class swch:
    def generate_signal(self, market_data):
        df = pd.DataFrame(market_data)

        price_change_threshold = 0.02  # 2% price change
        volume_spike_threshold = 1.5   # 50% volume increase compared to the average

        # price change percentage
        price_change = (df['last_price'].iloc[-1] - df['last_price'].iloc[0]) / df['last_price'].iloc[0]  

        avg_volume = df['volume'].mean()

        # check if sweep is significant enough
        if abs(price_change) > price_change_threshold and df['volume'].iloc[-1] > avg_volume * volume_spike_threshold:
            # check for CHoCH
            if price_change < 0:  # bearish sweep
                return {"action": "SELL", "symbol": "BTCUSDT", "qty": 1}
            elif price_change > 0:  # bullish sweep 
                return {"action": "BUY", "symbol": "BTCUSDT", "qty": 1}

        return None
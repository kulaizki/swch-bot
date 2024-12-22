import pandas as pd
import numpy as np

class Swch:
    def generate_signal(self, market_data):
        if market_data is None or 'result' not in market_data or 'list' not in market_data['result'] or not market_data['result']['list']:
            print("invalid or empty market data")
            return None

        df = pd.DataFrame(market_data['result']['list'])
        if df.empty:
            print("dataframe is empty")
            return None

        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms') # convert to datetime
        df = df.set_index('close_time') # set index

        df['close'] = pd.to_numeric(df['close']) # convert to numeric
        df['volume'] = pd.to_numeric(df['volume']) # convert to numeric
        df['open'] = pd.to_numeric(df['open']) # convert to numeric


        if len(df) < 2:  # need at least 2 data points
            return None

        price_change_threshold = 0.02  # 2% price change
        volume_spike_threshold = 1.5  # 50% volume increase

        # price change percentage
        price_change = (df['close'].iloc[-1] - df['close'].iloc[0]) / df['close'].iloc[0]

        avg_volume = df['volume'].mean()

        # check for sweep and choch
        if abs(price_change) > price_change_threshold and df['volume'].iloc[-1] > avg_volume * volume_spike_threshold:
            if price_change < 0:  # bearish sweep
                return {"action": "SELL", "symbol": "BTCUSDT", "qty": 1}
            elif price_change > 0:  # bullish sweep
                return {"action": "BUY", "symbol": "BTCUSDT", "qty": 1}

        return None
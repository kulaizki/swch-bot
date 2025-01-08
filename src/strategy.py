import pandas as pd
import numpy as np

class swch:
    def __init__(self, price_change_threshold=0.02, volume_spike_threshold=1.5):
        self.price_change_threshold = price_change_threshold
        self.volume_spike_threshold = volume_spike_threshold

    def generate_signal(self, market_data):
        if market_data is None or 'result' not in market_data or 'list' not in market_data['result'] or not market_data['result']['list']:
            print("invalid or empty market data")
            return None

        df = pd.DataFrame(market_data['result']['list'])
        if df.empty:
            print("dataframe is empty")
            return None

        # convert and set index
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        df = df.set_index('close_time')
        df = df[['open', 'close', 'volume']].apply(pd.to_numeric)

        # ensure 1-hour aggregation
        df = df.resample('1H').agg({
            'open': 'first',
            'close': 'last',
            'volume': 'sum'
        }).dropna()

        if len(df) < 2:  # need at least 2 data points
            print("not enough data for analysis")
            return None

        # calculate price change and average volume
        price_change = (df['close'].iloc[-1] - df['close'].iloc[0]) / df['close'].iloc[0]
        avg_volume = df['volume'].mean()

        # check for sweep and choch
        if abs(price_change) > self.price_change_threshold and df['volume'].iloc[-1] > avg_volume * self.volume_spike_threshold:
            if price_change < 0:  # bearish sweep
                return {"action": "SELL", "symbol": "BTCUSDT", "qty": 1}
            elif price_change > 0:  # bullish sweep
                return {"action": "BUY", "symbol": "BTCUSDT", "qty": 1}

        return None

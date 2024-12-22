class Strategy:
    def generate_signal(self, market_data):
        prices = [float(item["last_price"]) for item in market_data]
        volumes = [float(item["volume"]) for item in market_data]

        # threshold for liquidity sweep
        price_change_threshold = 0.02  # 2% price change
        volume_spike_threshold = 1.5   # 50% volume increase compared to the average

        price_change = (prices[-1] - prices[0]) / prices[0]  

        avg_volume = sum(volumes) / len(volumes)

        # check if sweep is significant enough
        if abs(price_change) > price_change_threshold and volumes[-1] > avg_volume * volume_spike_threshold:
            # check for CHoCH
            if price_change < 0: # bearish sweep
                return {"action": "SELL", "symbol": "BTCUSDT", "qty": 1}
            elif price_change > 0: # bullish sweep 
                return {"action": "BUY", "symbol": "BTCUSDT", "qty": 1}

        return None

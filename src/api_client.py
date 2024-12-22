import requests
from config.settings import API_KEY, API_SECRET, BASE_URL

class BybitAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.api_key = API_KEY
        self.api_secret = API_SECRET

    def get_market_data(self, symbol):
        endpoint = f"{self.base_url}/v2/public/tickers"
        response = requests.get(endpoint, params={"symbol": symbol})
        return response.json()

    def place_order(self, symbol, side, qty, order_type="Market"):
        endpoint = f"{self.base_url}/v2/private/order/create"
        payload = {
            "symbol": symbol,
            "side": side,
            "order_type": order_type,
            "qty": qty,
            "time_in_force": "GoodTillCancel",
            "api_key": self.api_key,
        }
        response = requests.post(endpoint, json=payload)
        return response.json()

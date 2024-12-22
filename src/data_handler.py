class DataHandler:
    def __init__(self, api_client):
        self.api_client = api_client

    def fetch_market_data(self, symbol):
        raw_data = self.api_client.get_market_data(symbol)
        return raw_data["result"]
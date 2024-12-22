class TradeExecutor:
    def __init__(self, api_client):
        self.api_client = api_client

    def execute_trade(self, signal):
        response = self.api_client.place_order(
            signal["symbol"], signal["action"], signal["qty"]
        )
        print(f"Trade executed: {response}")
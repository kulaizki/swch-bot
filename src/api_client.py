from pybit.unified_trading import HTTP
import os
from dotenv import load_dotenv

load_dotenv()  

class BybitAPI:
    def __init__(self, demo=True, testnet=False):
        api_key = os.getenv("DEMO_API_KEY" if demo else "API_KEY") 
        api_secret = os.getenv("DEMO_API_SECRET" if demo else "API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API_KEY or API_SECRET not set in environment variables.")

        self.client = HTTP(
            api_key=api_key,
            api_secret=api_secret,
            demo=demo,
            testnet=testnet,
        )

    def get_market_data(self, symbol):
        try:
            response = self.client.query_kline(symbol=symbol, interval="D")
            return response
        except Exception as e:
            print(f"Error fetching market data: {str(e)}")
            return None
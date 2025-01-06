import os
from dotenv import load_dotenv

load_dotenv()

def get_api_credentials(mode: str):
    """
    Retrieve API credentials based on the selected mode.
    """
    if mode == "demo":
        return os.getenv("DEMO_API_KEY"), os.getenv("DEMO_API_SECRET")
    elif mode == "testnet":
        return os.getenv("TESTNET_API_KEY"), os.getenv("TESTNET_API_SECRET")
    elif mode == "mainnet":
        return os.getenv("MAINNET_API_KEY"), os.getenv("MAINNET_API_SECRET")
    else:
        raise ValueError("Invalid mode. Choose 'demo', 'testnet', or 'mainnet'.")
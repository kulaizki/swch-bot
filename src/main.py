import argparse
import os
from dotenv import load_dotenv
from api_client import BybitAPI
from data_handler import DataHandler
from strategy import swch
from trade_executor import TradeExecutor
from logger import setup_logger

load_dotenv()

logger = setup_logger()

def load_api_credentials(mode):
    """
    Load API credentials based on the selected mode.
    """
    if mode == "demo":
        return os.getenv("DEMO_API_KEY"), os.getenv("DEMO_API_SECRET")
    elif mode == "testnet":
        return os.getenv("TESTNET_API_KEY"), os.getenv("TESTNET_API_SECRET")
    elif mode == "mainnet":
        return os.getenv("MAINNET_API_KEY"), os.getenv("MAINNET_API_SECRET")
    else:
        logger.error("Invalid mode selected.")
        return None, None

def main(mode):
    logger.info(f"Starting bot in {mode} mode...")

    api_key, api_secret = load_api_credentials(mode)
    if not api_key or not api_secret:
        logger.error("API credentials not found for the selected mode.")
        return

    if mode == "demo":
        api = BybitAPI(api_key, api_secret, demo=True, testnet=False)
    elif mode == "testnet":
        api = BybitAPI(api_key, api_secret, demo=False, testnet=True)
    elif mode == "mainnet":
        api = BybitAPI(api_key, api_secret, demo=False, testnet=False)

    data_handler = DataHandler(api)
    strategy = swch()
    executor = TradeExecutor(api)

    market_data = data_handler.fetch_market_data("BTCUSDT")
    signal = strategy.generate_signal(market_data)
    if signal:
        logger.info(f"Generated Signal: {signal}")
        executor.execute_trade(signal)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trading bot for Bybit.")
    parser.add_argument(
        "--mode",
        choices=["demo", "testnet", "mainnet"],
        default="testnet",  
        help="Select the mode: 'demo', 'testnet', or 'mainnet'. Default is 'testnet'."
    )
    args = parser.parse_args()
    main(args.mode)
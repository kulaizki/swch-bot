import argparse
from config.settings import get_api_credentials
from api_client import BybitAPI
from data_handler import DataHandler
from strategy import swch
from trade_executor import TradeExecutor
from logger import setup_logger

logger = setup_logger()

def main(mode):
    logger.info(f"Starting bot in {mode} mode...")
    
    try:
        api_key, api_secret = get_api_credentials(mode)
    except ValueError as e:
        logger.error(str(e))
        return
    
    if not api_key or not api_secret:
        logger.error(f"API credentials not set for {mode} mode.")
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
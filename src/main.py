import argparse
from api_client import BybitAPI
from data_handler import DataHandler
from strategy import swch
from trade_executor import TradeExecutor
from logger import setup_logger

logger = setup_logger()

def main(mode):
    logger.info("Starting bot...")
    if mode == "demo":
        api = BybitAPI(demo=True, testnet=False)
    elif mode == "testnet":
        api = BybitAPI(demo=False, testnet=True)
    elif mode == "mainnet":
        api = BybitAPI(demo=False, testnet=False)
    else:
        logger.error("Invalid mode selected. Choose 'demo', 'testnet', or 'mainnet'.")
        return

    data_handler = DataHandler(api)
    strategy = swch()
    executor = TradeExecutor(api)

    market_data = data_handler.fetch_market_data("BTCUSDT")
    signal = strategy.generate_signal(market_data)
    if signal:
        logger.info(f"Generated Signal: {signal}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trading bot for Bybit.")
    parser.add_argument(
        "--mode",
        choices=["demo", "testnet", "mainnet"],
        default="testnet",  
        help="Select the mode: 'demo', 'testnet', or 'mainnet'. Default is 'demo'."
    )
    args = parser.parse_args()
    main(args.mode)
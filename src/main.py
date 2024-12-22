from src.api_client import BybitAPI
from src.data_handler import DataHandler
from src.swch import swch
from src.trade_executor import TradeExecutor
from src.logger import setup_logger

logger = setup_logger()


def main():
    logger.info("Starting bot...")
    api = BybitAPI(demo=True, testnet=False)  
    data_handler = DataHandler(api)
    strategy = swch()
    executor = TradeExecutor(api)

    market_data = data_handler.fetch_market_data("BTCUSDT")
    signal = strategy.generate_signal(market_data)
    if signal:
        logger.info(f"Generated Signal: {signal}")  

if __name__ == "__main__":
    main()
from api_client import BybitAPI
from data_handler import DataHandler
from strategy import swch
from trade_executor import TradeExecutor
from logger import setup_logger

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
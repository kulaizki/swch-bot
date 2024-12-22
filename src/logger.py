import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

def setup_logger():
    logger = logging.getLogger("BotLogger")
    logger.setLevel(logging.INFO)  

    file_handler = logging.FileHandler("logs/bot.log")
    file_handler.setLevel(logging.INFO)  

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
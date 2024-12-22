# swch-bot (Liquidity Sweep & ChoCH Trading Bot - Experimental)

This is a Python script designed to automate algorithmic trading on Bybit using the Bybit API. The bot focuses on identifying and capitalizing on:

*   **Liquidity Sweeps:** When large orders rapidly move through price levels, potentially creating an opportunity to enter or exit a trade.
*   **Change of Character (ChoCH):** Shifts in price momentum that may signal a potential trend reversal.

**Disclaimer:** This is an experimental script and should not be considered financial advice. Always conduct thorough testing and understand the risks involved before deploying any trading bot with real capital.

**Requirements:**

*   Python 3.x
*   `pybit` library (installation: `pip install pybit`)
*   Bybit API credentials (obtainable from your Bybit account)

**Instructions:**

1.  **Install dependencies:** Run `pip install pybit` in your terminal.
2.  **Set environment variables:** Create a `.env` file in the same directory as the script and add the following lines, replacing `<YOUR_API_KEY>` and `<YOUR_API_SECRET>` with your actual Bybit API credentials:

    ```
    DEMO_API_KEY=<YOUR_API_KEY>
    DEMO_API_SECRET=<YOUR_API_SECRET>
    ```

3.  **Run the script:** Execute the Python script from your terminal.

**Note:** This is a basic framework. Further development is required to implement specific trade logic, risk management strategies, and order execution.

**Additional Resources:**

*   Bybit API Documentation: [https://www.bybit.com/future-activity/en/developer](https://www.bybit.com/future-activity/en/developer)
*   Liquidity Sweeps Explained: [https://www.fluxcharts.com/](https://www.fluxcharts.com/)
*   Understanding Price Action: [https://www.tradingview.com/script/CnB3fSph-Smart-Money-Concepts-SMC-LuxAlgo/](https://www.tradingview.com/script/CnB3fSph-Smart-Money-Concepts-SMC-LuxAlgo/)

**Disclaimer (again):** This script is provided for educational purposes only. Use it at your own risk. Always prioritize responsible trading practices and conduct your own research before using any automated trading tool.

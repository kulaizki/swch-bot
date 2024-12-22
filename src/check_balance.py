from pybit.unified_trading import HTTP
import os
from dotenv import load_dotenv

load_dotenv()

DEMO_API_KEY = os.getenv("DEMO_API_KEY")
DEMO_API_SECRET = os.getenv("DEMO_API_SECRET")

if not DEMO_API_KEY or not DEMO_API_SECRET:
    raise ValueError("DEMO_API_KEY or DEMO_API_SECRET not set in environment variables.")

try:
    session = HTTP(
        api_key=DEMO_API_KEY,
        api_secret=DEMO_API_SECRET,
        demo=True,
        testnet=False
    )

    def get_total_wallet_balance(account_type):
        try:
            response = session.get_wallet_balance(accountType=account_type)

            if response and 'retCode' in response and response['retCode'] == 0:
                if 'result' in response and 'list' in response['result']:
                    total_balance = 0
                    for item in response['result']['list']:
                        total_balance += float(item.get('totalWalletBalance', 0))
                    return total_balance
                else:
                    print("Error: 'list' key not found in response data")
                    return None
            elif response and 'retMsg' in response:
                print(f"API Error: {response['retMsg']}")
                return None
            else:
                print("Error: Invalid API response format")
                return None

        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return None

    if __name__ == "__main__":
        account_type = "UNIFIED"
        total_balance = get_total_wallet_balance(account_type)

        if total_balance is not None:
            print(f"Total Wallet Balance (USD): {total_balance}")
        else:
            print("Failed to retrieve total wallet balance.")

except Exception as e:
    print(f"Initialization Error: {e}")
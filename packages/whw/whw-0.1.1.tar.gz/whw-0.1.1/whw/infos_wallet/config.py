import requests
import threading
import time
from decimal import Decimal

def _get_ether_price() -> dict:
    url = "https://api.coingecko.com/api/v3/coins/ethereum"
    try:
        resp = requests.get(url)
        data = resp.json()
        price_eth = {
            'USD': data['market_data']['current_price']['usd'],
            'EUR': data['market_data']['current_price']['eur'],
            'BTC': data['market_data']['current_price']['btc']
        }
        return price_eth
    except requests.RequestException as e:
        raise Exception("Erreur lors de la récupération du prix de l'ether") from e

def _refresh_price():
    global PRICE_ETH
    while True:
        PRICE_ETH = _get_ether_price()
        time.sleep(600)  # Wait for 10 minutes (600 seconds)

def start_price_refresh_thread():
    thread = threading.Thread(target=_refresh_price)
    thread.daemon = True  # Daemonize thread
    thread.start()

# Initialize the global variable
global PRICE_ETH
PRICE_ETH = _get_ether_price()
ROUNDING_PRECISION = Decimal('0.001')
start_price_refresh_thread()

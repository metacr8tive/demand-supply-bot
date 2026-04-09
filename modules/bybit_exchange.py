import requests

class BybitExchange:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://api.bybit.com'

    def get_market_data(self, symbol):
        endpoint = f'/v2/public/tickers?symbol={symbol}'
        response = requests.get(self.base_url + endpoint)
        return response.json()

    def get_account_info(self):
        endpoint = '/v2/private/account/get
        params = {'api_key': self.api_key}
        response = requests.get(self.base_url + endpoint, params=params)
        return response.json()

    def place_order(self, symbol, qty, order_type, price=None):
        endpoint = '/v2/private/order/create'
        params = {
            'api_key': self.api_key,
            'symbol': symbol,
            'order_type': order_type,
            'qty': qty,
            'price': price
        }
        response = requests.post(self.base_url + endpoint, params=params)
        return response.json()

    def get_futures_market_data(self, symbol):
        endpoint = f'/futures/v2/public/tickers?symbol={symbol}'
        response = requests.get(self.base_url + endpoint)
        return response.json()

    def get_trade_history(self, symbol):
        endpoint = f'/v2/private/order/list'
        params = {'api_key': self.api_key, 'symbol': symbol}
        response = requests.get(self.base_url + endpoint, params=params)
        return response.json()
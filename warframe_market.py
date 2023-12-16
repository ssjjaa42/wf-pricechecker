import urllib.request
import json


class WarframeMarket:

    def __init__(self, api_key: str):
        """
        Initialize this WarframeMarket object.

        :param apikey: The Cookie API Key to use.
        """
        self.__key = api_key

    def search_item(self, item: str, platform='pc'):
        item_id = item.lower().replace(' ', '_')
        url = f'https://api.warframe.market/v1/items/{item_id}'
        request_site = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0',
                                                            'Platform': platform})
        web_url = urllib.request.urlopen(request_site)
        resp = json.loads(web_url.read().decode(web_url.info().get_content_charset('utf-8')))
        if resp.get('error'):
            error_msg = resp['error']
            raise LookupError(error_msg)
        return resp['payload']['item']['items_in_set']

    def search_buy_orders(self, item: str, platform='pc', results=5):
        """
        Searches the Warframe Market and returns a list of the best (price) buy orders available.

        :param item: The name of the item to look for, ex. "Garuda Prime Neuroptics Blueprint"
        :param platform: The platform to look on. Can be one of ('pc', 'xbox', 'ps4', 'switch'), defaults to 'pc'
        :param results: The number of results to return, defaults to 5
        :raises LookupError: If something has gone wrong with the URL request
        :return: A list of the top buy orders available
        """
        item_id = item.lower().replace(' ', '_')
        url = f'https://api.warframe.market/v1/items/{item_id}/orders'
        request_site = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0',
                                                            'Cookie': f'JWT={self.__key}',
                                                            'Platform': platform})
        web_url = urllib.request.urlopen(request_site)
        try:
            resp = json.loads(web_url.read().decode(web_url.info().get_content_charset('utf-8')))
        except json.decoder.JSONDecodeError:
            raise ValueError('Invalid item name.')
        if resp.get('error'):
            error_msg = resp['error']
            raise LookupError(error_msg)
        buy_orders = []
        for order in resp['payload']['orders']:
            if order['order_type'] == 'buy':
                buy_orders.append(order)
        buy_orders.sort(key=lambda o: o['platinum'], reverse=True)
        best_orders = []
        # Add the best in-game buy orders to the list of best orders
        for order in buy_orders:
            if order['user']['status'] == 'ingame':
                best_orders.append(order)
            if len(best_orders) == results:
                break
        # Add the best online buy orders to the list of best orders, if needed
        if len(best_orders) < results:
            for order in buy_orders:
                if order['user']['status'] == 'online':
                    best_orders.append(order)
                if len(best_orders) == results:
                    break
        # Add the best offline buy orders to the list of best orders, if needed
        if len(best_orders) < results:
            for order in buy_orders:
                if order['user']['status'] == 'offline':
                    best_orders.append(order)
                if len(best_orders) == results:
                    break
        return best_orders

import json

import requests

from config import keys


class ConvertExeption(Exception):
    pass


class Converter:
    @staticmethod
    def converter(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertExeption(f"Нельзя перевести одинаковые валюты {base}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertExeption(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertExeption(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertExeption(f"Не удалось обработать {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base

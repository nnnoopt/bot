import json

import requests
from telebot import types

from config import keys


class ConvertExeption(Exception):
    pass


class Line_of_buttons:
    def __init__(self, keys: list, number_line_of_buttons=0):
        self.number_line_of_buttons = number_line_of_buttons
        self.keys = keys
        self.markup = types.InlineKeyboardMarkup(row_width=1)
    @property
    def get_markup(self):
        for i in range(len(self.keys)):
            self.item = types.InlineKeyboardButton(self.keys[i],
                                                   callback_data=self.keys[i] + str(self.number_line_of_buttons))
            self.markup.add(self.item)

        return self.markup


class Converter:
    @staticmethod
    def converter(quote: str, base: str, amount: str):


        try:
            amount = float(amount)
        except ValueError:
            raise ConvertExeption(f"Не удалось обработать {amount}")


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}')
        total_base = json.loads(r.content)[base] * amount

        return total_base

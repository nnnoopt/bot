import json

import requests
from telebot import types


class ConvertExeption(Exception):
    pass


class Line_of_buttons:
    def __init__(self, keys: list, number_of_line_buttons=0):
        self.__number_of_line_buttons = number_of_line_buttons
        self.__keys = keys
        self.__markup = types.InlineKeyboardMarkup(row_width=1)

    @property
    def get_markup(self):

        for i in range(len(self.__keys)):
            self.__item = types.InlineKeyboardButton(self.__keys[i],
                                                     callback_data=self.__keys[i] + str(self.__number_of_line_buttons))
            self.__markup.add(self.__item)

        return self.__markup

    @property
    def get_callback_data(self):
        check = []
        for i in range(len(self.__keys)):
            check.append(self.__keys[i] + str(self.__number_of_line_buttons))
        return check


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

import telebot
from telebot import types

from config import keys, TOKEN

from utils import Converter, ConvertExeption

bot = telebot.TeleBot(TOKEN)


quote = ""
base = ""


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    msg = "Выбери название валюты, которую хочешь узнать:"

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("USD", callback_data='USD')
    item2 = types.InlineKeyboardButton("EUR", callback_data='EUR')
    item3 = types.InlineKeyboardButton("RUB", callback_data='RUB')
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, f"Привет , {message.chat.username}!\n{msg}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global base
    global quote

    if call.data == 'USD':
        quote = 'доллар'
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("USD", callback_data='USD1')
        item2 = types.InlineKeyboardButton("EUR", callback_data='EUR1')
        item3 = types.InlineKeyboardButton("RUB", callback_data='RUB1')
        markup1.add(item1, item2, item3)

        bot.send_message(call.message.chat.id, 'введи валюту', reply_markup=markup1)
    if call.data == 'EUR':
        quote = 'евро'
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("USD", callback_data='USD1')
        item2 = types.InlineKeyboardButton("EUR", callback_data='EUR1')
        item3 = types.InlineKeyboardButton("RUB", callback_data='RUB1')
        markup1.add(item1, item2, item3)

        bot.send_message(call.message.chat.id, 'введи валюту', reply_markup=markup1)
    if call.data == 'RUB':
        quote = 'рубль'
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("USD", callback_data='USD1')
        item2 = types.InlineKeyboardButton("EUR", callback_data='EUR1')
        item3 = types.InlineKeyboardButton("RUB", callback_data='RUB1')
        markup1.add(item1, item2, item3)

        bot.send_message(call.message.chat.id, 'введи валюту', reply_markup=markup1)

    if call.data == 'USD1':
        base = 'доллар'

        bot.send_message(call.message.chat.id, 'введи количество')
    if call.data == 'EUR1':
        base = 'евро'

        bot.send_message(call.message.chat.id, 'введи количество')
    if call.data == 'RUB1':
        base = 'рубль'
        bot.send_message(call.message.chat.id, 'введи количество')


@bot.message_handler(content_types=['text', ])
def conv(message):
    global base
    global quote

    amount = message.text
    total_base = Converter.converter(quote, base, amount)
    text = f"цена {amount} {quote} в {base} - {total_base}"
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling(none_stop=True)

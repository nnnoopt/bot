import telebot
from telebot import types

from config import keys, TOKEN

from utils import Converter, ConvertExeption

bot = telebot.TeleBot(TOKEN)

count = 0
quote = ''
base = ''


def buttons():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("USD", callback_data='USD')
    item2 = types.InlineKeyboardButton("EUR", callback_data='EUR')
    item3 = types.InlineKeyboardButton("RUR", callback_data='RUB')
    return markup.add(item1, item2, item3)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    msg = "Выбери название валюты, которую хочешь узнать:"

    markup = buttons()
    bot.send_message(message.chat.id, f"Привет , {message.chat.username}!\n{msg}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global count
    # global quote
    # global base

    if count == 0:
        # if call.data == 'USD':
        #     quote = 'доллар'
        # if call.data == 'EUR':
        #     quote = 'евро'
        # if call.data == 'RUR':
        #     quote = 'рубль'
        # quote = 'доллар'
        markup1 = buttons()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введите валюту в которой необходимо узнать:",
                              reply_markup=markup1)


    if count == 1:
        count -= 1

        # if call.data == 'USD':
        #     base = 'доллар'
        # if call.data == 'EUR':
        #     base = 'евро'
        # if call.data == 'RUR':
        #     base = 'рубль'

        # base = 'евро'

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введите количество валюты:")


@bot.message_handler(commands=['values'])
def handle_values(message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key,))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text', ])
def conv(message):
    #     try:
    #         values = message.text.split(' ')
    #
    #         if len(values) != 3:
    #             raise ConvertExeption("Слишком много параметров.")
    #
    #         quote, base, amount = values
    #
    #         total_base = Converter.converter(quote, base, amount)
    #     except ConvertExeption as e:
    #         bot.send_message(message.chat.id, f"Ошибка пользователя\n {e}")
    #     except Exception as e:
    #         bot.send_message(message.chat.id, f"Не удалось обработать команду\n {e}")
    #     else:
    #         text = f"цена {amount} {quote} в {base} - {total_base}"
    #         bot.send_message(message.chat.id, text)

    amount = int(message.text)
    total_base = Converter.converter(str(quote), str(base), str(amount))
    text = f"цена {amount} {quote} в {base} - {total_base}"
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

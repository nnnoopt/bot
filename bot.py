import telebot

from config import keys, TOKEN

from utils import Converter, ConvertExeption, Line_of_buttons

bot = telebot.TeleBot(TOKEN)

quote = ""
base = ""


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    msg = "Выбери название валюты, которую хочешь узнать:"

    buttons1 = Line_of_buttons(keys, number_line_of_buttons=1)

    bot.send_message(message.chat.id, f"Привет , {message.chat.username}!\n{msg}", reply_markup=buttons1.get_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global base
    global quote
    buttons2 = Line_of_buttons(keys, number_line_of_buttons=2)

    if call.data == 'USD1':
        quote = 'USD'

        bot.send_message(call.message.chat.id, 'введи валюту', reply_markup=buttons2.get_markup)
    if call.data == 'EUR1':
        quote = 'EUR'

        bot.send_message(call.message.chat.id, 'введи валюту', reply_markup=buttons2.get_markup)
    if call.data == 'RUB1':
        quote = 'RUB'

        bot.send_message(call.message.chat.id, 'введи валюту', reply_markup=buttons2.get_markup)

    if call.data == 'USD2':
        base = 'USD'

        bot.send_message(call.message.chat.id, 'введи количество')
    if call.data == 'EUR2':
        base = 'EUR'

        bot.send_message(call.message.chat.id, 'введи количество')
    if call.data == 'RUB2':
        base = 'RUB'
        bot.send_message(call.message.chat.id, 'введи количество')


@bot.message_handler(content_types=['text', ])
def conv(message):
    global base
    global quote

    amount = message.text

    try:
        total_base = Converter.converter(quote, base, amount)
        text = f"цена {amount} {quote} в {base} - {total_base}"
        bot.send_message(message.chat.id, text)
    except ConvertExeption:
        bot.send_message(message.chat.id, 'Введено не число')


if __name__ == '__main__':
    bot.polling(none_stop=True)

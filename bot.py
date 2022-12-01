import telebot

from config import keys, TOKEN

from utils import Converter, ConvertExeption, Line_of_buttons

bot = telebot.TeleBot(TOKEN)

quote = ""
base = ""
check1 = []
check2 = []


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    global check1
    msg = "Выбери валюту из которой нужно получить:"

    buttons1 = Line_of_buttons(keys, number_of_line_buttons=1)
    check1 = buttons1.get_callback_data

    bot.send_message(message.chat.id, f"Привет , {message.chat.username}!\n{msg}", reply_markup=buttons1.get_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global base
    global quote
    global check1
    global check2

    if call.data in check1:
        quote = call.data[:3]
        buttons2 = Line_of_buttons(keys, number_of_line_buttons=2)
        bot.send_message(call.message.chat.id, 'Выбери валюту которую нужно получить', reply_markup=buttons2.get_markup)
        check2 = buttons2.get_callback_data
    elif call.data in check2:
        base = call.data[:3]
        bot.send_message(call.message.chat.id, 'Введи количество')


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
        bot.send_message(message.chat.id, 'Введи число')


if __name__ == '__main__':
    bot.polling(none_stop=True)

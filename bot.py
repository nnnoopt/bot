import telebot

from config import keys, TOKEN

from utils import Converter, ConvertExeption

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    msg = "Введи название валюты, которую хочешь узнать:\n" \
          "Bмя валюты, в которой надо узнать цену первой валюты.\n" \
          "Количество первой валюты.\n" \
          "Список валют: /values"

    bot.send_message(message.chat.id, f"Привет , {message.chat.username}!\n{msg}")


@bot.message_handler(commands=['values'])
def handle_values (message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key,))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text', ])
def conv(message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertExeption("Слишком много параметров.")

        quote, base, amount = values

        total_base = Converter.converter(quote, base, amount)
    except ConvertExeption as e:
        bot.send_message(message.chat.id, f"Ошибка пользователя\n {e}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Не удалось обработать команду\n {e}")
    else:
        text = f"цена {amount} {quote} в {base} - {total_base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

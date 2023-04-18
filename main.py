import telebot
from config import public_currency_keys, telegram_token
from utils import ConversionException, CurrencyConverter

bot = telebot.TeleBot(telegram_token)


@bot.message_handler(commands=['start', 'help'])
def show_help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате: \n <имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \
Увидеть список доступных валют /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in public_currency_keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        message.text = message.text.lower()
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException("Слишком много параметров.")
        base, quote, amount = values

        total_base = CurrencyConverter.get_price(quote, base, amount)

    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n {e} ')
    else:
        text = f'{amount} {base} эквивалентно {round(total_base, 2)} {quote}'
        bot.send_message(message.chat.id, text)


bot.polling()

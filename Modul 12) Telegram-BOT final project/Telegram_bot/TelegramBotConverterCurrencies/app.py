import telebot
from config import currencies, TOKEN
from extensions import CryptoConverter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message) -> None:
    '''
    Функция обрабатывает команды start и help
    :param message: telebot.types.Message
    :return: None
    '''
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message) -> None:
    '''
    Функция обрабатывает команду values
    :param message: telebot.types.Message
    :return: None
    '''
    line = "Доступные валюты:\n"
    line += '\n'.join(currencies.keys())
    bot.reply_to(message, line)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message) -> None:
    '''
    Функция конвертации валют
    :param message: telebot.types.Message
    :return: None
    '''
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException(f'Неверный формат ввода данных. /help')

        quote, base, amount = values

        if quote == base:
            raise APIException(f'Вы ввели одинаковые валюты.\nФормат ввода данных: /help')

        if not currencies.get(quote):
            raise APIException(f'Валюта \"{quote}\" не существует.\nФормат ввода данных: /help')

        if not currencies.get(base):
            raise APIException(f'Валюта \"{base}\" не существует.\nФормат ввода данных: /help')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Значение \"<количество переводимой валюты>\" должно быть числом.\nФормат ввода данных: /help')

    except APIException as e:
        bot.reply_to(message, f'Ошибка ввода:\n{e}')
    else:
        result = CryptoConverter.get_price(quote, base, amount)
        bot.reply_to(message, f'{amount} \"{quote}\" в \"{base}\" = {result}')


bot.polling(none_stop=True)
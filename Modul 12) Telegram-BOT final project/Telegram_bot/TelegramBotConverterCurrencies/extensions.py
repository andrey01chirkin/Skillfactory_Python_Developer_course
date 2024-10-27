import json
import requests
from config import currencies

class APIException(Exception):
    '''
    Класс для обработки исключений.
    '''
    pass

class CryptoConverter:
    '''
    Класс для отправки запросов к API.
    '''

    @staticmethod
    def get_price(quote: str, base: str, amount: str) -> float:
        if quote == base:
            raise APIException(f'Вы ввели одинаковые валюты.\nФормат ввода данных: /help')

        if not currencies.get(quote):
            raise APIException(f'Валюта \"{quote}\" не существует.\nФормат ввода данных: /help')

        if not currencies.get(base):
            raise APIException(f'Валюта \"{base}\" не существует.\nФормат ввода данных: /help')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Значение <количество переводимой валюты> должно быть числом.\nФормат ввода данных: /help')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={currencies[quote]}&tsyms={currencies[base]}')
        value = json.loads(r.content)
        return amount * value[currencies[base]]


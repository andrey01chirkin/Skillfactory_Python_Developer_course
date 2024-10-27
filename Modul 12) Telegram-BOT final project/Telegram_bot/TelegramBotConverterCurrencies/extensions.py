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
    def get_price(quote: str, base: str, amount: float) -> float:
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={currencies[quote]}&tsyms={currencies[base]}')
        currency = json.loads(r.content)
        return amount * currency[currencies[base]]


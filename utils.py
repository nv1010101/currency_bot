import requests
import json
from config import keys, url


class ConversionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_temp = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}')

        try:
            base_temp = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except KeyError:
            raise ConversionException(f'Не удалось обработать количество {amount}')

        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        d = json.loads(response.content)
        print(d)
        dict_rates = d["rates"]

        conversion_result = (dict_rates[keys[quote]] * amount) / (dict_rates[keys[base]])

        return conversion_result

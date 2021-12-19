from django.http.response import JsonResponse
from rest_framework.views import APIView
from decimal import *
import requests
import json

class CoinConverter(APIView):
    """
    API that receives two coins and an amount as input
    and convert from one coin to another

    :params 
            - ?from: coin that will be converted
            - ?to: result converted coin
            - ?amount: amount from the coin that will be converted to a new one
    :return - converted coin from first coin param to second
    """

    def get(self, request, *args, **kwargs) -> JsonResponse:
        try:
            from_coin = request.query_params['from']
            to_coin = request.query_params['to']
            coin_amount = request.query_params['amount']

    
            formated_coin_amount = self.format_number(coin_amount)
            currency_obj = Currency(from_coin)
            converted_coin = currency_obj.convert_to_currency(to_coin, formated_coin_amount)

            json_data = {
                'from_coin': from_coin,
                'to_coin': to_coin,
                'coin_amount': formated_coin_amount,
                'converted_coin_amount': converted_coin
                }
        except:
            return JsonResponse(status=404, data={'status': 'false', 'message': 'Invalid url params'})

        return JsonResponse(data=json_data)
    
    def format_number(self, number) -> str:
        try:
            formated_number = str(float(number))

            return formated_number
        except:
            
            return 'Invalid data'

class Currency():
    """
    Class implements a currency object and
    implements methods to convert it to other currencies

    :params
            -?currency_code - three letters code that represents the currency name,
             possible choices can be found at the URL below
             https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json
    """

    def __init__(self, currency_code):
        self.currency_code = currency_code.lower()

    def convert_to_usd(self, amount):
        url= f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{self.currency_code}.json'
        response = requests.get(url)
        dict_response = json.loads(response.text)
        currency_in_usd = Decimal(str(dict_response[self.currency_code]['usd']))

        return currency_in_usd * Decimal(str(amount))

    def convert_usd_to_currency(self, final_currency):
        cleaned_data_currency = final_currency.lower()
        url= f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json'
        response = requests.get(url)
        dict_response = json.loads(response.text)
        usd_to_currency = Decimal(str(dict_response['usd'][cleaned_data_currency]))

        return usd_to_currency

    def convert_to_currency(self, to_currency, amount):
        currency_in_usd = self.convert_to_usd(amount)
        usd_to_currency = self.convert_usd_to_currency(to_currency)

        return currency_in_usd * usd_to_currency

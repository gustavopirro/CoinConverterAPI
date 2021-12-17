from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView


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
        except:
            return JsonResponse(status=404, data={'status': 'false', 'message': 'Invalid url params'})

        return JsonResponse({'from_coin': from_coin, 'to_coin': to_coin, 'coin_amount': coin_amount})
    
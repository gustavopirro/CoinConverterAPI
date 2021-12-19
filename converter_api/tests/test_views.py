from rest_framework.test import APITestCase
from django.urls import reverse
import json

class TestConverter(APITestCase):

    def test_get_coin_converter(self):
        api_url = reverse('converter_api:coin_converter')
        response = self.client.get(api_url,
            {
            'from': 'USD',
            'to': 'BRL',
            'amount': 1
            })
        dict_response = json.loads(response.content)


        self.assertEquals(response.status_code, 200)
        self.assertEquals(type(dict_response['converted_coin_amount']), type(str()))
        self.assertIsNotNone(response)

    
    def test_get_converter_status_code_invalid_data(self):
        api_url = reverse('converter_api:coin_converter')
        response = self.client.get(api_url, {
            'from': 'USD',
            'to': 'BTC',
            'amount': 'invalid amount'
        })

        self.assertEquals(response.status_code, 404)
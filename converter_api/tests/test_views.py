from rest_framework.test import APITestCase
from django.urls import reverse

class TestConverter(APITestCase):

    def test_get_converter_status_code(self):
        api_url = reverse('converter_api:coin_converter')
        response = self.client.get(
            api_url,
            {
            'from': 'BRL',
            'to': 'USD',
            'amount': 1
            })

        self.assertEquals(response.status_code, 200)
    
    def test_get_converter_status_code_invalid_data(self):
        api_url = reverse('converter_api:coin_converter')
        response = self.client.get(api_url)

        self.assertEquals(response.status_code, 404)
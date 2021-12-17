from django.urls import path
from . import views

app_name = 'converter_api'

urlpatterns = [
    ### REST API ###
    path('coinconverter', views.CoinConverter.as_view(), name='coin_converter'),
]
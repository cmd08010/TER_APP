from django.test import TestCase
from django.test import Client
import json
from unittest import mock
from .models import Prices
from datetime import datetime, date


class PricesTestCase(TestCase):
  def setUp(self):
    self.factory = Client()

  @mock.patch('prices.models.date')
  def test_we_get_the_latest_price_with_a_price(self, mock_date):
    mock_date.today.return_value = date(2022, 3, 7)

    good_schedule = {
        "date":"2022-03-07",
        "prices": [
            {"datetime":"2022-03-08T0:0:0+0000","price":"12.34"},
            {"datetime":"2022-03-08T0:1:0+0000","price":"23.45"},
            {"datetime":"2022-03-08T0:2:0+0000","price":"34.56"}
        ]
     }

    Prices.objects.create(schedule=good_schedule, created='2022-03-02')

    Prices.objects.create(schedule={
        "date":"2022-03-07",
        "prices": [
            {"datetime":"2022-03-08T0:0:0+0000","price":"13.34"},
            {"datetime":"2022-03-08T0:1:0+0000","price":"23.45"},
            {"datetime":"2022-03-08T0:2:0+0000","price":"34.56"}
        ]
    }, created='2022-03-01')

    response = self.factory.get('/prices/today/')
    print(response)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, good_schedule)

  @mock.patch('prices.models.date')  
  def test_we_get_404_with_no_latest_price(self, mock_date):
    mock_date.today.return_value = date(2022, 2, 7)

    good_schedule = {
        "date":"2022-03-07",
        "prices": [
            {"datetime":"2022-03-08T0:0:0+0000","price":"12.34"},
            {"datetime":"2022-03-08T0:1:0+0000","price":"23.45"},
            {"datetime":"2022-03-08T0:2:0+0000","price":"34.56"}
        ]
      }

    Prices.objects.create(schedule=good_schedule, created='2022-03-02')

    Prices.objects.create(schedule={
        "date":"2022-03-07",
        "prices": [
            {"datetime":"2022-03-08T0:0:0+0000","price":"13.34"},
            {"datetime":"2022-03-08T0:1:0+0000","price":"23.45"},
            {"datetime":"2022-03-08T0:2:0+0000","price":"34.56"}
        ]
    }, created='2022-03-01')

    response = self.factory.get('/prices/today/')

    self.assertEqual(response.status_code, 404)





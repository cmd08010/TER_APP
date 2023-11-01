from django.test import TestCase
from django.test import Client
import json
from unittest import mock
from .models import Device
from ven.models import VEN
from datetime import datetime, date


class DevicesTestCase(TestCase):
  def setUp(self):
    self.factory = Client()

  def test_create_device_with_existing_ven(self):
    VEN.objects.create(id="TEST_VEN_1") 
    device = {
        "ven_id": "TEST_VEN_1",
        "device_id": "TEST_DEVICE_1",
        "statusOn": True,
        "registerConsumed": "99.00",
        "registerProduced": "0.00"
    }
    response = self.factory.post('/devices/', data=device)
    saved = Device.objects.get(device_id='TEST_DEVICE_1')
    self.assertEqual(saved.device_id, device["device_id"])
    self.assertEqual(saved.ven_id.id, device["ven_id"])
    self.assertEqual(response.status_code, 201)
    device_response =  {
        "id": 1,
        "device_id": "TEST_DEVICE_1",
        "ven_id": "TEST_VEN_1",
        "statusOn": True,
        "registerConsumed": "99.00",
        "registerProduced": "0.00"
    }
    self.assertEqual(response.data, device_response)

  def test_create_with_nonexisting_ven(self):
    device = {
        "ven_id": "TEST_VEN_NEW",
        "device_id": "TEST_DEVICE_2",
        "statusOn": True,
        "registerConsumed": "99.00",
        "registerProduced": "0.00"
    }
    response = self.factory.post('/devices/', data=device)
    self.assertEqual(response.status_code, 201)
    saved = Device.objects.get(device_id='TEST_DEVICE_2')
    self.assertEqual(saved.device_id, device["device_id"])
    self.assertEqual(saved.ven_id.id, device["ven_id"])
    device_response =  {
        "id": 2,
        "device_id": "TEST_DEVICE_2",
        "ven_id": "TEST_VEN_NEW",
        "statusOn": True,
        "registerConsumed": "99.00",
        "registerProduced": "0.00"
    }
    self.assertEqual(response.data, device_response)

  def test_update_device(self):
    ven = VEN.objects.create(id="TEST_VEN_UPDATE") 
    device = {
        "ven_id": ven,
        "device_id": "TEST_DEVICE_3",
        "statusOn": True,
        "registerConsumed": "99.00",
        "registerProduced": "0.00"
    }
    Device.objects.create(**device)
    payload = {
        "ven_id": "TEST_VEN_UPDATE",
        "device_id": "TEST_DEVICE_3",
        "statusOn": False,
    }
    response = self.factory.put('/devices/3/', data=payload, follow=True,content_type='application/json')
    self.assertEqual(response.status_code, 200)
    saved = Device.objects.get(device_id='TEST_DEVICE_3')
    self.assertEqual(saved.device_id, device["device_id"])
    self.assertEqual(saved.ven_id, ven)
    self.assertEqual(saved.statusOn, False)
    device_response =  {
        "id": 3,
        "device_id": "TEST_DEVICE_3",
        "ven_id": "TEST_VEN_UPDATE",
        "statusOn": False,
        "registerConsumed": "99.00",
        "registerProduced": "0.00"
    }
    self.assertEqual(response.data, device_response)
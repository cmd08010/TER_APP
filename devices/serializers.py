from django.forms import CharField
from rest_framework import serializers
from devices.models import Device
from ven.models import VEN
from ven.serializers import VENSerializer

import logging

logger = logging.getLogger('ter')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'device_id', 'ven_id', 'statusOn', 'registerConsumed', 'registerProduced']
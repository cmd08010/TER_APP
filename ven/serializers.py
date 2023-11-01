from rest_framework import serializers
from .models import VEN

#TODO: serailize related devices 

class VENSerializer(serializers.ModelSerializer):
    class Meta:
        model = VEN
        fields = ['id', 'statusOn', 'token', 'devices']
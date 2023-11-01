from rest_framework import serializers
from meters.models import Meters


class MetersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meters
        fields = ['id', 'created', 'meters']
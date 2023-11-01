from rest_framework import serializers
from prices.models import Prices


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ['created', 'schedule']
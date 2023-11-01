from prices.models import Prices
from prices.serializers import PricesSerializer
from rest_framework import generics, response, status
from rest_framework import permissions
from rest_framework.views import APIView
import logging
from datetime import datetime, date 

logger = logging.getLogger('ter')

date_format = ""

# GET /prices/latest

# GET /prices?date=2022-03-22

class PricesLatest(APIView):
    def get(self, request, format=None):
        latest_price = Prices.latest()
        return response.Response(latest_price) if latest_price else response.Response(status=status.HTTP_404_NOT_FOUND)
  

# GET /prices
# POST /prices
class PricesList(generics.ListCreateAPIView):
    logger.info("PricesList: view")

    permission_classes = [permissions.IsAuthenticated]

    queryset = Prices.objects.all()
    serializer_class = PricesSerializer

# GET /<id>
class PricesDetail(generics.RetrieveUpdateDestroyAPIView):
    logger.info("PricesDetail: view")

    permission_classes = [permissions.IsAuthenticated]

    queryset = Prices.objects.all()
    serializer_class = PricesSerializer
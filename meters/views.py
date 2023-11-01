from meters.models import Meters
from meters.serializers import MetersSerializer
from rest_framework import generics
import logging
from rest_framework import permissions

class MetersList(generics.ListCreateAPIView):
    # logger example
    logger = logging.getLogger('ter')
    logger.info("MetersList: I'm here")

    # TBD: re-create users/groups
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Meters.objects.all()
    serializer_class = MetersSerializer


class MetersDetail(generics.RetrieveUpdateDestroyAPIView):
    # TBD: re-create users/groups
    # permission_classes = [permissions.IsAuthenticated]

    queryset = Meters.objects.all()
    serializer_class = MetersSerializer
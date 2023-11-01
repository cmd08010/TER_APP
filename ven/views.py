from django.shortcuts import render
from .models import VEN
from ven.serializers import VENSerializer
from rest_framework import generics
import logging

#TODO: check if VEN token matches what is sent from the VTN 

logger = logging.getLogger('ter')

class VenDetail(generics.ListAPIView):
    logger.info("VEN Detail: view")

    # permission_classes = [permissions.IsAuthenticated]

    #queryset = VEN.objects.all()
    serializer_class = VENSerializer 

    def get_queryset(self):
        ven_token = self.kwargs['ven_token']
        return VEN.objects.filter(token=ven_token)

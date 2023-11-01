# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the devices index.")

# def detail(request, device_id):
#     return HttpResponse("Details of  %s." % device_id)

# def status(request, device_id):
#     return HttpResponse("Status of  %s." % device_id)

from site import venv
from devices.models import Device
from ven.models import VEN
from devices.serializers import DeviceSerializer
from rest_framework import generics
import logging
from rest_framework import permissions

logger = logging.getLogger('ter')

class DeviceList(generics.ListCreateAPIView):
    logger.info("DeviceList: view")

    # permission_classes = [permissions.IsAuthenticated]

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def post(self, request, *args, **kwargs):
     ven = VEN.objects.get_or_create(id=request.data['ven_id'])
     return  self.create(request, *args, **kwargs)



class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
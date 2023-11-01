"""API for Meters model"""
from meters.models import Meters
import logging

logger = logging.getLogger('ter')

class MetersAPI:
    """API for Meters model"""
    def create_meter():
        # m = Meters(meters='{ "meterID": "99", "VEN_ID": "99", "device_id": "99" }')
        # m.save()
        pass

    def get_meter(device_id):
        """Traverse Meters to find item with device_id"""
        print(f"MetersAPI.get_meter(device_id={device_id})")
        logger.info(f"MetersAPI.get_meter(device_id={device_id})")
        for q in Meters.objects.all():
            print(q.meters)
            if device_id == q.meters['device_id']:
                return q.meters

        return({ "meterID": "dummy", "VEN_ID": "dummy", "device_id": "dummy" })

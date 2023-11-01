from django.db import models
from ven.models import VEN
#TODO: devices ven_id is now a foreign key to VEN model 

class Device(models.Model):
    device_id = models.CharField(max_length=80)
    ven_id = models.ForeignKey(VEN, on_delete=models.SET_NULL, null=True)
    statusOn = models.BooleanField(default=True)
    registerConsumed = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    registerProduced = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        unique_together = ('device_id', 'ven_id',)

    def __str__(self):
        return str(self.device_id)
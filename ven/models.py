from django.db import models

class VEN(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    statusOn = models.BooleanField(default=True)
    token = models.CharField(max_length=80)

    def __str__(self):
        return str(self.id)
from django.db import models

class Meters(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    meters = models.JSONField()
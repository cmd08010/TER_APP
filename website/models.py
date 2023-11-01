from django.db import models


class Register(models.Model):
    register_type = models.CharField(max_length=250)
    member_name = models.CharField(max_length=250)
    account_address = models.CharField(max_length=250)
    account_number = models.CharField(max_length=250)
    member_email = models.CharField(max_length=250)
    member_phone = models.CharField(max_length=250)
    # Device fields
    ven_id = models.CharField(max_length=250)
    device_id = models.CharField(max_length=250)
    device_type = models.CharField(max_length=250)
    # Aggregator fields
    company = models.CharField(max_length=250, blank=True)
    aggregator_name = models.CharField(max_length=250, blank=True)
    aggregator_email = models.CharField(max_length=250, blank=True)
    aggregator_phone = models.CharField(max_length=250, blank=True)
    # Logs fields
    date = models.DateTimeField(auto_now_add=True)


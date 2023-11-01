from website.models import Register 
from datetime import timedelta
from django.utils import timezone 
from celery import shared_task

@shared_task
def remove_old_records():
    time_threshold = timezone.now() - timedelta(days=14)
    records = Register.objects.filter(date__lt=time_threshold)
    records.delete()

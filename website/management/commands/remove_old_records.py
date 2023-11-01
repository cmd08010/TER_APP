from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from website.models import Register

class Command(BaseCommand):
    help = 'Clears records older than 14 days'

    def handle(self, *args, **options):
        time_threshold = timezone.now() - timedelta(days=14)
        records = Register.objects.filter(date__lt=time_threshold)
        records.delete()
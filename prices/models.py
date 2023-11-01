from django.db import models
from datetime import datetime, date
#TODO: refactor to seperate into actual columns 

class Prices(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    schedule = models.JSONField()
    date_format = '%Y-%m-%d'

    @classmethod
    def latest(self):
        prices = self.objects.all().order_by('created')
        latest_prices = [ p.schedule for p in prices if datetime.strptime(p.schedule['date'], self.date_format).date() == date.today() ] 

        return latest_prices[0] if latest_prices else None


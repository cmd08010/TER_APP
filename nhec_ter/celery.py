from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nhec_ter.settings')

app = Celery('nhec_ter')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'UTC'

@app.task(bind=True)
def debug_task(self):
    print('this task!')
    print('Request: {0!r}'.format(self.request))

#run everyday at 5am-ish 
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'website.tasks.remove_old_records',
        'schedule': 10.0,
    },
}

 #Load task modules from all registered Django app configs.
app.autodiscover_tasks()
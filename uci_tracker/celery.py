from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uci_tracker.settings')

from django.conf import settings  # noqa

app = Celery('uci_tracker')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('uci_tracker.celeryconfig')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
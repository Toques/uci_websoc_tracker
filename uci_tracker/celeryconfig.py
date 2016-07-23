BROKER_URL = 'amqp://'
CELERY_TIMEZONE = 'America/Los_Angeles'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'courses.tasks.refresh_courses',
        'schedule': timedelta(seconds=30),
    },
}
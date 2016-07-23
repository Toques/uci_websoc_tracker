BROKER_URL = 'amqp://dyykxxau:RNU9IDsx0vN3hR8DJ5m6soUWxSA1FBu5@wildboar.rmq.cloudamqp.com/dyykxxau'
CELERY_TIMEZONE = 'America/Los_Angeles'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'courses.tasks.refresh_courses',
        'schedule': timedelta(seconds=30),
    },
}
web: gunicorn uci_tracker.wsgi --log-file -
worker: python manage.py celery worker -B -l info
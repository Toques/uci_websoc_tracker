web: gunicorn uci_tracker.wsgi --log-file -
worker: celery -A app.tasks worker --loglevel=info --concurrency=1
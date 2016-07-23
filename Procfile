web: gunicorn uci_tracker.wsgi --log-file -
worker: celery -A myapp worker -l info -B -b amqp://dyykxxau:RNU9IDsx0vN3hR8DJ5m6soUWxSA1FBu5@wildboar.rmq.cloudamqp.com/dyykxxau
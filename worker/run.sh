poetry install && \
    AMQP=amqp://guest:guest@127.0.0.1:5672/ BACKEND=mongodb://root:example@127.0.0.1:27017/celery \
    poetry run watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- celery -- -A worker.app  worker -- -l info
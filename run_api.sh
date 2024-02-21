cd api && poetry install && \
    AMQP=amqp://guest:guest@127.0.0.1:5672/ BACKEND=mongodb://root:example@127.0.0.1:27017/celery \
    poetry run uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload
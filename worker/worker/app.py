from celery import Celery
import os
import time

amqp = os.environ["AMQP"]
backend = os.environ["BACKEND"]

app = Celery("tasks", broker=amqp, backend=backend)


@app.task(name="add")
def add(x, y):
    time.sleep(10)
    return x + y

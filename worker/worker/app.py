from celery import Celery
import os
import time
from worker.pi_calc import calculate_pi

amqp = os.environ["AMQP"]
backend = os.environ["BACKEND"]

app = Celery("tasks", broker=amqp, backend=backend)


@app.task(name="calculate_pi")
def calculate_pi_task(precision: int):
    return calculate_pi(precision)


@app.task(name="add")
def add(x, y):
    time.sleep(10)
    return x + y

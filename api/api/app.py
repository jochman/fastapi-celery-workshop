import os
from fastapi import FastAPI
from celery import Celery

amqp = os.environ["AMQP"]
backend = os.environ["BACKEND"]

celery = Celery("tasks", broker=amqp, backend=backend)

app = FastAPI()


@app.post("/add")
async def get_number(x: float, y: float):
    task = celery.send_task("tasks.add", kwargs={"x": x, "y": y})
    return task.id


@app.get("result/{task_id}")
async def get_results(task_id: str):
    result = celery.AsyncResult(task_id)
    if result.state == "SUCCESS":
        return result.get()
    return {"id": task_id, "state": result.state}

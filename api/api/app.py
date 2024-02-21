import os
from fastapi import FastAPI
from celery import Celery

amqp = os.environ["AMQP"]
backend = os.environ["BACKEND"]

celery = Celery("tasks", broker=amqp, backend=backend)

app = FastAPI()


@app.post("/add")
async def get_number(x: float, y: float):
    task = celery.send_task("add", kwargs={"x": x, "y": y})
    return {"task-id": task.id}


@app.get("/pi/{precision}")
async def calculate_pi(precision: int):
    task = celery.send_task("calculate_pi", args=(precision,))
    return {"task-id": task.id}


@app.get("/result/{task_id}")
async def get_results(task_id: str):
    result = celery.AsyncResult(task_id)
    resp = {"task-id": task_id, "state": result.state}
    if result.state == "SUCCESS":
        resp["result"] = result.get()
        return resp
    return resp

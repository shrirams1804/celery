from dcelery.celery_config import app
import logging
from celery import Task,group,chain
import time


@app.task(queue='tasks')
def add(x,y):
    return x+y

@app.task(queue='tasks')
def multiply(result):
    # simulate an error for demonstration purpose
    if result == 0:
        raise ValueError("Error: Division by zero.")
    return result*2

def run_task_chain():
    # creating chain
    task_chain = chain(add.s(2,3),multiply.s())
    result = task_chain.apply_async()
    result.get()


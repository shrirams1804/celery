from dcelery.celery_config import app
import time


@app.task(queue='tasks')
def my_task1():
    pass
    

@app.task(queue='tasks')
def my_task2():
    pass
    
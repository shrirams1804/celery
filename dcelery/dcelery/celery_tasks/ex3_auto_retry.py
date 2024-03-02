from dcelery.celery_config import app
import logging
from celery import Task
import time

logging.basicConfig(filename='app.log',level=logging.ERROR,format='%(actime)s %(levelname)s %(message)s')


class CustomTask(Task):
    def on_failure(self,exc,task_id,args,kwargs,einfo):
        # to handle task failure
        # capturing connection error
        if isinstance(exc,ConnectionError):
            logging.error("Connection error occured-Admin notified")
        else:
            print('{0!r} failed: {1!r}'.format(task_id,exc))

app.Task = CustomTask

@app.task(queue='tasks',autretry_for=(ConnectionError,),default_retry_delay=5,retry_kwargs={'max_retries':5})
def my_task():
    raise ConnectionError("Connection Error Occured.........")
    return
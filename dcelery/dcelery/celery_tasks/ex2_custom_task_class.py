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

@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError("Connection Error Occured...")
    except ConnectionError:
        raise ConnectionError()
        # task does not complete
        # raise ConnectionError()
    except ValueError:
        logging.error("Value erro ocurred....")
        perform_specific_error_handling()
    except Exception:
        # handling generic exception
        logging.erro("An error occured")
        # notify administrator to perform fallback action
        notify_admins()
        perfom_fallback_action()
def perform_specific_error_handling():
    pass
def notify_admins():
    # notify administrator 
    pass
def perfom_fallback_action():
    # to perform fallback action
    pass
    


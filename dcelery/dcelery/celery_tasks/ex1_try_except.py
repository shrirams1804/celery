from dcelery.celery_config import app
import logging
import time

logging.basicConfig(filename='app.log',level=logging.ERROR,format='%(actime)s %(levelname)s %(message)s')

@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError("Connection Error Occured...")
    except ConnectionError:
        logging.error("Connection error occured....")
        # task does not complete
        # raise ConnectionError()
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
    


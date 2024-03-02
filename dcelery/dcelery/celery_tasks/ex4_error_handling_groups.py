from dcelery.celery_config import app
import logging
from celery import Task,group
import time

# logging.basicConfig(filename='app.log',level=logging.ERROR,format='%(actime)s %(levelname)s %(message)s')


# class CustomTask(Task):
#     def on_failure(self,exc,task_id,args,kwargs,einfo):
#         # to handle task failure
#         # capturing connection error
#         if isinstance(exc,ConnectionError):
#             logging.error("Connection error occured-Admin notified")
#         else:
#             print('{0!r} failed: {1!r}'.format(task_id,exc))

# app.Task = CustomTask

@app.task(queue='tasks')
def my_task(number):
    if number == 3:
        raise ValueError("Error number is invalid")
    return number * 2

# we need a function which is going to handle,every result from each task
def handle_result(result):
    if result.successful():
        # successful returns True if all the subtasks finished successfully
        print(f"Task Completed:{result.get}")
    elif result.failed() and isinstance(result.result,ValueError):
        print(f"Task Failed: ,{result.result}")
    elif result.status == 'REVOKED':
        print(f"Task was revoked: {result.id}")

def run_tasks():
    task_group = group(my_task.s(i) for i in range(5))
    # running task group
    result_group = task_group.apply_async()
    # to get the result of each task within the group ,
    # we are using get method on async result object
    result_group.get(disable_sync_subtasks=False,propagate=False)

    for result in result_group:
        handle_result(result)
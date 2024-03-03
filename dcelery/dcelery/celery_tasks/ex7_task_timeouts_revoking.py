from celery import group
from dcelery.celery_config import app
import time
import sys

# time is in seconds
@app.task(queue="tasks",time_limit=10)
def long_running_task():
    time.sleep(6)
    return "Task completed successfully"

@app.task(queue="tasks",bind=True)
def process_task_result(self,result):
    if result is None:
        return "Task was revoked,skipping result processing"
    else:
        return f"Task result:{result}"

# this is not celery task
def execute_task_examples():
    result = long_running_task.delay()
    try:
        task_result = result.get(timeout=40)
    except TimeoutError:
        print("Task time out")

    task = long_running_task.delay()
    task.revoke(terminate=True)
    # time delay to get revoked else we get PENDING
    time.sleep(3)
    # after revoke we will check the status of task
    sys.stdout.write(task.status)#PENDING # our task is running
    # if you are thinking task status should be REVOKED => important considerations => if you are revoking tasks, in this case it is showing PENDING,because you are retriving the status immediately after revoking the task
    # when we call revoke here,it initaites the revokation process, revokation process takes time to propogate and update the status of the task and thats important to rememeber, so here it is showing PENDING, because revokation process not yet completed.
    # task status will eventually change to revoked once the revocation is fully processed
    # we will modifyt the code and add time delay of 3 sec
    if task.status == 'REVOKED':
        process_task_result.delay(None)# task was revoked,process accoordingly
    else:
        process_task_result.delay(task.result)
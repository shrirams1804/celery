from celery import group
from dcelery.celery_config import app


app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True

@app.task(queue='tasks')
def my_task(z):
    try:
        if z == 2:
            raise ValueError("Error wrong number..........")
    except Exception as e:
        # traceback_str = traceback.format_exc()
        # task_id = my_task.request.id
        # we will move this task to another queue if it fails
        handle_failed_task.apply_async(args=((z),str(e)))
        # to show in flower it is failed task
        raise

@app.task(queue='dead_letter')
def handle_failed_task(z,exception):
    return "Custom logic to process"

# when the task does fail,it is indeed then sent to the dead letter queue
def run_task_group():
    task_group = group(
        my_task.s(1),
        my_task.s(2),
        my_task.s(3),
    )
    task_group.apply_async()
   
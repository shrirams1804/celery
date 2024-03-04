from datetime import timedelta
# timedelta to get time differences
from dcelery.celery_config import app

"""
app.conf.beat_schedule = {
    'task1':{
        'task':'dcelery.celery_tasks.ex12_task_schedule_customization.task1',
        # we set here run this task every 5 seconds
        'schedule':timedelta(seconds=5),
        'kwargs':{'foo':'bar'},
        'args':(18,4),
        'options':{
            'queue':'tasks',
            'priory':5,
        }
    },
    'task2':{
        'task':'dcelery.celery_tasks.ex12_task_schedule_customization.task2',
        # we set here run this task every 10 seconds
        'schedule':timedelta(seconds=10),
    }
}
"""
# we need to trigger these tasks at specific interval, we will setup that in our schedular
# we need to specify the interval, that is time wait before we execute the task again
@app.task(queue="tasks")
def task1(a=10,b=14,**kwargs):
    result = a + b
    print(f"Running task 1 {result}")

@app.task(queue="tasks")
def task2():
    print("Running task 2 ")
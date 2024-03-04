
from datetime import timedelta
# timedelta to get time differences
from dcelery.celery_config import app
from celery.schedules import crontab


app.conf.beat_schedule = {
    # 'task1':{
    #     'task':'dcelery.celery_tasks.ex13_task_schedule_crontab.task1',
    #     # we set here run this task every 5 seconds
    #     'schedule':crontab(minute='0-59/1', hour='0-18', day_of_week='mon'),
    #     'kwargs':{'foo':'bar'},
    #     'args':(18,4),
    #     'options':{
    #         'queue':'tasks',
    #         'priory':5,
    #     }
    # },
    # 'task2':{
    #     'task':'dcelery.celery_tasks.ex13_task_schedule_crontab.task2',
    #     # we set here run this task every 10 seconds
    #     'schedule':timedelta(seconds=10),
    # }
}
# we need to trigger these tasks at specific interval, we will setup that in our schedular
# we need to specify the interval, that is time wait before we execute the task again
@app.task(queue="tasks")
def task1(a,b,**kwargs):
    result = a + b
    print(f"Running task 1 {result}")

@app.task(queue="tasks")
def task2():
    print("Running task 2 ")

"""
* * * * *
| | | | | 
| | | | +----- Day of the week (0-6) (Sunday=0 or 7)
| | | +------- Month (1-12)
| | +--------- Day of the Month (1-31)
| +----------- Hour (0 - 23)
+------------- Minute (0 - 59)
"""
# in crontab time is considered in minutes
"""
* * * * *       # run every minute
*/5 * * * *     # run every 5 minutes
30 * * * *      # run every hour at 30 minutess past the hour
"""
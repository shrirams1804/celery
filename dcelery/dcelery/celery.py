import os
from celery import Celery
# Kombu is a messaging library for Python. It is an open-source project that provides a high-level interface to the Advanced Message Queuing Protocol (AMQP).
from kombu import Exchange, Queue
import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

# creating celery instance,created celery application
app = Celery("dcelery")
app.config_from_object("django.conf:settings",namespace="CELERY")

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),# 10 is highest prio,1 is lowest prio
]
# enables late acknowledgement task in celery
app.conf.task_acks_late = True

# general task will have priority
app.conf.task_default_priority = 5

# number of tasks fetched from brocker at once
app.conf.worker_prefetch_multiplier = 1

# tasks will get executed based on priority one at a time,
# only one worker process will be active at a time
app.conf.worker_concurrency = 1

@app.task(queue='tasks')
def t1(a,b,message=None):
    result = a+b
    time.sleep(3)
    if message:
        result = f"{message}:{result}"
    return result
@app.task(queue='tasks')
def t2():
    time.sleep(3)
    return 
@app.task(queue='tasks')
def t3():
    time.sleep(3)
    return 


# app.conf.task_routes = {
#     'newapp.tasks.*':{'queue':'queue1'},
#     'newapp.tasks.*':{'queue':'queue2'},
# }
# scheduling tasks based on priorities,priorities are from 0 to 9

# app.conf.task_default_rate_limit = '1/m'

# app.conf.broker_transport_options = {
#     'priority_steps':list(range(10)),
#     'sep':':',
#     'queue_order_strategy':'priority',
# }
app.autodiscover_tasks()

def test():
    # call asynchronously
    result = t1.apply_async(args=[5,10],kwargs={'message':"Hi Dear"})

    # check if task has completed
    if result.ready():
        print("Task has completed")
    else:
        print("Task is still running")
    
    # check if the task completed successfully
    if result.successful():
        print("Task Completed Successfully")
    else:
        print("Task encountered an error")

    # get the result of the task
    try:
        task_reuslt = result.get()
        print("Task result: ",task_reuslt)
    except Exception as e:
        print("An exception occured: ",str(e))

    # get the exception (if any) that ocuured during task exception
    exception = result.get(propagate=False)
    if exception:
        print("An error occured during task execution: ",str(exception)) 

    '''
    >>> from dcelery.celery import t1
    >>> from dcelery.celery import test
    >>> test()
    Task is still running
    Task encountered an error
    Task result:  Hi Dear:15
    An error occured during task execution:  Hi Dear:15
    '''
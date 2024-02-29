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
def t1():
    time.sleep(3)
    return 
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
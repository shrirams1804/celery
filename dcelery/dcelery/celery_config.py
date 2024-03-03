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
          queue_arguments={'x-max-priority': 10}),# 10 is highest prio,1 is lowest priority
    Queue('dead_letter',routing_key='dead_letter'),
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

# getting project directory
base_dir = os.getcwd()
# getting the tasks folder
task_folder = os.path.join(base_dir,'dcelery','celery_tasks')

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith('ex') and filename.endswith('.py'):
            module_name = f'dcelery.celery_tasks.{filename[:-3]}'
            module = __import__(module_name,fromlist=['*'])
            for name in dir(module):
                obj = getattr(module,name)
                if callable(obj) and name.startswith('my_tasks'):
                    task_modules.append(f'{module_name}.{name}')


    app.autodiscover_tasks(task_modules)

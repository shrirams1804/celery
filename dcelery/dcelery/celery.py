import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

# creating celery instance,created celery application
app = Celery("dcelery")
app.config_from_object("django.conf:settings",namespace="CELERY")
app.autodiscover_tasks()
app.conf.task_routes = {
    'newapp.tasks.task1':{'queue':'queue1'},
    'newapp.tasks.task2':{'queue':'queue2'},
}
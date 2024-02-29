import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

# creating celery instance,created celery application
app = Celery("dcelery")
app.config_from_object("django.conf:settings",namespace="CELERY")

# app.conf.task_routes = {
#     'newapp.tasks.*':{'queue':'queue1'},
#     'newapp.tasks.*':{'queue':'queue2'},
# }
# scheduling tasks based on priorities,priorities are from 0 to 9

app.conf.task_default_rate_limit = '1/m'

app.conf.broker_transport_options = {
    'priority_steps':list(range(10)),
    'sep':':',
    'queue_order_strategy':'priority',
}
app.autodiscover_tasks()
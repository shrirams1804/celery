from celery import shared_task
import time
from django.core.management import call_command

# we have mentioned which queue should be utilised
@shared_task()
# def management_command(queue='tasks'):
def management_command():
    # django is going to find this file and run command
    call_command("test_command")

# @shared_task
# def tp2(queue='celery:1'):
#     time.sleep(3)
#     return

# @shared_task
# def tp3(queue='celery:2'):
#     time.sleep(3)
#     return

# @shared_task
# def tp4(queue='celery:3'):
#     time.sleep(3)
#     return

from celery import shared_task
import requests
from sentry_sdk import capture_exception
import time

# this is celery task, if exception occured , it will get handled, so celery
# task will not be fail
@shared_task
def check_webpage():
    try:
        response = requests.get("http://127.0.0.1:8001")
        if response.status_code != 200:
            # celery wont raise this exception
            raise Exception("Website is down...lets panic!")
    except requests.exceptions.RequestException as e:
        # if there is an exception,grab that data and send that back to sentry
        capture_exception(e)
    return


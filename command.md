 > pip freeze > requirements.txt

 > docker-compose up -d --build

 To run docker container,
 > docker exec -it django /bin/sh
 > /user/src/app # ls
Dockerfile        db.sqlite3        dcelery           entrypoint.sh     manage.py         requirements.txt

 To create app in django project
/user/src/app # python manage.py startapp cworker

# Remove all docker
docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -aq)

 docker stop $(docker ps -aq) ; docker rm $(docker ps -aq) ; docker rmi $(docker images -aq)

# FOR Error Building wheel for backports.zoneinfo (pyproject.toml) did not run successfully.
# update requirements.txt
 backports.zoneinfo;python_version<"3.9"

 # you can get rabbitmq interface here,
 http://localhost:15672/#/


 from dcelery.celery import t1,t2,t3
 t2.apply_async(priority=5)
 t1.apply_async(priority=6)
 t3.apply_async(priority=9)
 t2.apply_async(priority=5)
 t1.apply_async(priority=6)
 t3.apply_async(priority=9)

in terminal,run on dajngo to inspect task
celery inspect active
celery inspect active_queues

# passing arguments and returining result from celery task
>>> from dcelery.celery import t1,t2,t3
>>> t1.apply_async(args=[5,10],kwargs={'message':"Hi Dear"})
<AsyncResult: c5c07bfa-8d72-4d69-856e-67d482e57e57>
>>> result = t1.apply_async(args=[5,10],kwargs={'message':"Hi Dear"})
>>> result.get()
'Hi Dear:15'

>>> from dcelery.celery import t1
>>> from dcelery.celery import test
>>> test()
Task is still running
Task encountered an error
Task result:  Hi Dear:15
An error occured during task execution:  Hi Dear:15


# using custom task classes,error handling
from dcelery.celery_tasks.ex2_custom_task_class import my_task
my_task.delay()

# using custom task classes,retry
>>> from dcelery.celery_tasks.ex3_auto_retry import my_task
>>> my_task.delay()

# error handling in groups
>>> from dcelery.celery_tasks.ex4_error_handling_groups import run_tasks
>>> run_tasks()
Task Completed:<bound method AsyncResult.get of <AsyncResult: c57dea1e-aca7-443a-9044-0b1ce5ee72ce>>
Task Completed:<bound method AsyncResult.get of <AsyncResult: 3d1f9b6a-17ef-4605-a38e-25aa7f3614cc>>
Task Completed:<bound method AsyncResult.get of <AsyncResult: ed0f4ee2-a7f6-4730-90f3-143d29686dcf>>
Task Failed: ,Error number is invalid
Task Completed:<bound method AsyncResult.get of <AsyncResult: 9bbea174-81fe-492b-b796-5565329e4e9b>>

# error handling in task chaining
>>> from dcelery.celery_tasks.ex5_error_handling_chain import run_task_chain
>>> run_task_chain()

# dead letter queus,handling failed tasks
>>> from dcelery.celery_tasks.ex6_dead_letter_queue import run_task_group
>>> run_task_group()

# task timeouts and task revoking
>>> from dcelery.celery_tasks.ex7_task_timeouts_revoking import long_running_task
>>> long_running_task()
>>> long_running_task.delay()

# handling errors in task result callbacks
from dcelery.celery_tasks.ex8_linking_result_callbacks import run_task

# handling error in task result callbacks
>>> from dcelery.celery_tasks.ex8_linking_result_callbacks import run_task
>>> run_task()

# task signals graceful shtdown and cleanup of failed tasks
>>> from dcelery.celery_tasks.ex9_task_signals_graceful_shutdown_and_cleanup import run_task
>>> run_task()

# error tacking and monitoring with sentry
from dcelery.celery_tasks.ex10_error_tracking_and_monitoring_with_sentry import divide_numbers
divide_numbers.delay(10,0)


## Error
1:00 https://docs.celeryq.dev/en/latest/internals/protocol.html
2024-03-04 19:21:00 for more information.
2024-03-04 19:21:00 
2024-03-04 19:21:00 The full contents of the message body was:
2024-03-04 19:21:00 '[[18, 4], {"foo": "bar"}, {"callbacks": null, "errbacks": null, "chain": null, "chord": null}]' (94b)
2024-03-04 19:21:00 
2024-03-04 19:21:00 The full contents of the message headers:
2024-03-04 19:21:00 {'argsrepr': '[18, 4]', 'eta': None, 'expires': None, 'group': None, 'group_index': None, 'id': '62845044-296d-4161-9032-dfbbef74be9b', 'ignore_result': False, 'kwargsrepr': "{'foo': 'bar'}", 'lang': 'py', 'origin': 'gen13@6bb6b17e52d2', 'parent_id': None, 'replaced_task_nesting': 0, 'retries': 0, 'root_id': '62845044-296d-4161-9032-dfbbef74be9b', 'shadow': None, 'stamped_headers': None, 'stamps': {}, 'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task1', 'timelimit': [None, None]}
2024-03-04 19:21:00 
2024-03-04 19:21:00 The delivery info for this task is:
2024-03-04 19:21:00 {'consumer_tag': 'None4', 'delivery_tag': 1, 'redelivered': False, 'exchange': '', 'routing_key': 'tasks'}
2024-03-04 19:21:00 Traceback (most recent call last):
2024-03-04 19:21:00   File "/usr/local/lib/python3.11/site-packages/celery/worker/consumer/consumer.py", line 658, in on_task_received
2024-03-04 19:21:00     strategy = strategies[type_]
2024-03-04 19:21:00                ~~~~~~~~~~^^^^^^^
2024-03-04 19:21:00 KeyError: 'dcelery.celery_tasks.ex13_task_schedule_crontab.task1'
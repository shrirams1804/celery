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
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
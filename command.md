 > pip freeze > requirements.txt

 > docker-compose up -d --build

 To run docker container,
 > docker exec -it django /bin/sh
 > /user/src/app # ls
Dockerfile        db.sqlite3        dcelery           entrypoint.sh     manage.py         requirements.txt

 To create app in django project
/user/src/app # python manage.py startapp cworker
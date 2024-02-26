FROM python:3.11.4-alpine

WORKDIR /user/src/app

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
COPY ./requirements.txt /user/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /user/src/app/entrypoint.sh

COPY . /user/src/app/

ENTRYPOINT [ "/user/src/app/entrypoint.sh" ]
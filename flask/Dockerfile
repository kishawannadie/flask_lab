FROM tiangolo/meinheld-gunicorn-flask:python3.9-alpine3.13

RUN apk update && apk add --no-cache postgresql-dev gcc musl-dev

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app /app/app
COPY app/__init__.py /app/app/main.py
COPY common /app/common
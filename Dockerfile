FROM python:3.11-slim-bookworm

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install

COPY . .

ENV SECRET_KEY=default

RUN pipenv run python manage.py runserver 0.0.0.0:8000


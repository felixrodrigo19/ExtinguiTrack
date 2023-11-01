FROM Python:3.11

RUN pipenv install

RUN python manager runserver

#!/bin/bash

rm -r -f python_project/blog/migrations

python python_project/manage.py makemigrations blog

python python_project/manage.py migrate blog

rm -r -f python_project/db.sqlite3

python python_project/manage.py migrate

python python_project/manage.py createsuperuser --username 1234 --email test@test.com
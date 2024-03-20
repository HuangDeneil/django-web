#!/bin/sh 

python3.10 manage.py makemigrations
python3.10 manage.py migrate


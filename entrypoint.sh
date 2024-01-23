#!bin/sh
python manage.py makemigrations api
python manage.py migrate --no-input
python manage.py test
python manage.py populate && python manage.py runserver 0.0.0.0:8000 && fg
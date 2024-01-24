#!bin/sh
CONTAINER_FIRST_STARTUP="CONTAINER_FIRST_STARTUP"
if [ ! -e /$CONTAINER_FIRST_STARTUP ]; then
    touch /$CONTAINER_FIRST_STARTUP

    #Below should run only for the first time while creating the container
    python manage.py makemigrations api
    python manage.py migrate --no-input
    python manage.py test
    python manage.py populate && python manage.py runserver 0.0.0.0:8000 && fg
else
    python manage.py runserver 0.0.0.0:8000
fi

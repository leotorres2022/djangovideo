#!/bin/bash
if [ ! -f  manage.py ]
 then
  django-admin startproject app .
fi

sleep 2
python manage.py makemigrations
python manage.py migrate --noinput

if [ -n "$DJANGO_SU_NAME" ]; then
  # Crear superusuario sólo si no existe
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='${DJANGO_SU_NAME}').exists() or User.objects.create_superuser('${DJANGO_SU_NAME}', '${DJANGO_SU_EMAIL}', '${DJANGO_SU_PASSWORD}')" | python manage.py shell
fi

# Finalmente, arrancar el servidor de desarrollo y mantener el contenedor en primer plano
python manage.py runserver 0.0.0.0:8000
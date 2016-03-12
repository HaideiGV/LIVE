web: python manage.py migrate
web: python manage.py collectstatic --noinput
web: gunicorn --bind 0.0.0.0:${PORT:-8000} liveproject.wsgi

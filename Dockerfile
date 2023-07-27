FROM python:3.10.0

WORKDIR /home/

RUN echo "testing0001"

RUN git clone https://github.com/LikeIvy/pinterest.git

WORKDIR /home/pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pinterest.settings.deploy && python manage.py migrate --settings=pinterest.settings.deploy && gunicorn pinterest.wsgi --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy --bind 0.0.0.0:8000"]
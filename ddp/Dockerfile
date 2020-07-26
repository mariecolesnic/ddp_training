FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . ./
COPY ./config/uwsgi/uwsgi.ini /etc/

RUN pip install -r requirements.txt
CMD ["uwsgi", "--ini", "/config/uwsgi.ini"]
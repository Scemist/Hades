FROM ubuntu

COPY ./app /srv/app
WORKDIR /srv

RUN apt update
RUN apt install -y \
	python3 \
	python3-pip

RUN pip3 install virtualenv && \
	virtualenv .env

RUN . /srv/.env/bin/activate && \
	pip install gunicorn flask && \
	deactivate

WORKDIR /srv/app

ENTRYPOINT . /srv/.env/bin/activate && gunicorn -b 0.0.0.0:5000 wsgi:app
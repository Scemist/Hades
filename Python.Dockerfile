FROM alpine

COPY ./app /srv/app
WORKDIR /srv

RUN apk add \
	python3 \
	py3-pip

RUN pip3 install virtualenv && \
	virtualenv .env

RUN . /srv/.env/bin/activate && \
	pip install gunicorn flask && \
	deactivate

WORKDIR /srv/app

ENTRYPOINT . /srv/.env/bin/activate && python __init__.py
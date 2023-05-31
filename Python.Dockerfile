FROM alpine:3.18

COPY ./app /srv/app
WORKDIR /srv

RUN apk add \
	python3 \
	py3-pip

RUN pip3 install virtualenv && \
	virtualenv .env

RUN . /srv/.env/bin/activate && \
	pip install gunicorn flask && \
	pip install pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib && \
	deactivate

WORKDIR /srv/app

ENTRYPOINT . /srv/.env/bin/activate && python __init__.py
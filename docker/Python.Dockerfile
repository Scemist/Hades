FROM alpine:3.18

COPY . /srv/app
WORKDIR /srv

RUN apk add \
	python3 \
	py3-pip \
	gpg

RUN pip3 install virtualenv && \
	virtualenv .env

RUN . /srv/.env/bin/activate && \
	pip install --upgrade \
	gunicorn \
	flask \
	google-api-python-client \
	google-auth-httplib2 \
	google-auth-oauthlib \
	python-gnupg && \
	deactivate

RUN export AUTHLIB_RELAX_TOKEN_SCOPE=1

WORKDIR /srv/app

ENTRYPOINT . /srv/.env/bin/activate && \
	python __init__.py
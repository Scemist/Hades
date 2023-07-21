FROM alpine:3.18

COPY . /srv/app
WORKDIR /srv

RUN apk add \
	python3 \
	py3-pip \
	gpg \
	npm

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

RUN npm install --omit=dev
RUN npm run build

ENTRYPOINT . /srv/.env/bin/activate && \
	gunicorn -b 0.0.0.0:5000 __init__:app
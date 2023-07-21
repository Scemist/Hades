FROM alpine:3.18

RUN apk add npm
RUN export NODE_ENV=development

WORKDIR /srv/app

ENTRYPOINT npm install && npm run dev
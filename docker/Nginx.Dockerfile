FROM nginx:1.23.3-alpine

COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf
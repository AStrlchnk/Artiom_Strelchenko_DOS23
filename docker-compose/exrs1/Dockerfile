FROM ubuntu:20.04

RUN apt-get update && apt-get install nginx -y && apt-get install curl -y

RUN mkdir -p /app/static

COPY custom.conf /etc/nginx/

COPY /app/static /app/static

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/custom.conf"]

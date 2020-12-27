FROM debian AS poodlab

WORKDIR /root

RUN apt-get update && apt-get install -y curl tcpdump
COPY poodled.crt /usr/local/share/ca-certificates/poodled.crt
RUN update-ca-certificates


FROM nginx AS catwoman

WORKDIR /root

RUN apt-get update && apt-get install -y iproute2

COPY nginx.conf /etc/nginx/nginx.conf
COPY poodled.crt /etc/ssl/certs/poodled.crt
COPY poodled.key /etc/ssl/private/poodled.key

FROM debian AS batman

WORKDIR /root

RUN apt-get update && apt-get install -y curl
COPY poodled.crt /usr/local/share/ca-certificates/poodled.crt
RUN update-ca-certificates

###

FROM debian AS joker

WORKDIR /root

RUN apt-get update && apt-get install -y python3-scapy python3-cryptography
COPY poodle.py .

###

FROM nginx AS catwoman

WORKDIR /root

RUN apt-get update && apt-get install -y iproute2

COPY nginx.conf /etc/nginx/nginx.conf
COPY poodled.crt /etc/ssl/certs/poodled.crt
COPY poodled.key /etc/ssl/private/poodled.key

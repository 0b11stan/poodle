FROM debian:jessie AS batman

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

FROM debian:jessie AS catwoman

WORKDIR /root

RUN apt-get update && apt-get install -y openssl
COPY poodled.crt /root/poodled.crt
COPY poodled.key /root/poodled.key

###

FROM httpd AS catwoman-nginx

WORKDIR /root

RUN apt-get update && apt-get install -y iproute2

COPY nginx.conf /etc/nginx/nginx.conf
COPY poodled.crt /etc/ssl/certs/poodled.crt
COPY poodled.key /etc/ssl/private/poodled.key

###

FROM httpd AS catwoman-apache

RUN apt-get update && apt-get install -y iproute2
RUN sed -i 's/-SSLv3//' conf/extra/httpd-ssl.conf
RUN sed -i 's/^ServerName.*/ServerName catwoman:443/' conf/extra/httpd-ssl.conf
RUN sed -i 's/^#\(Include.*httpd-ssl.conf\)/\1/' conf/httpd.conf
RUN sed -i 's/^#LoadModule ssl_module/LoadModule ssl_module/' conf/httpd.conf
RUN sed -i 's/^#LoadModule socache_shmcb_module/LoadModule socache_shmcb_module/' conf/httpd.conf

COPY poodled.crt /usr/local/apache2/conf/server.crt
COPY poodled.key /usr/local/apache2/conf/server.key

WORKDIR /root

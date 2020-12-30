FROM debian:jessie AS openssl-ssl3

COPY sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y zlib1g-dev zlib1g
RUN apt-get install -y devscripts build-essential make zlib1g-dev libxml2-dev
RUN mkdir -p /_apt/
RUN cd /_apt/ && apt-get source openssl
RUN apt-get -y build-dep openssl
RUN sed -i 's/no-ssl2 no-ssl3/enable-ssl3/' /_apt/openssl-1.0.1t/debian/rules
RUN cd /_apt/openssl-1.0.1t/ && debuild -b -uc -us
RUN cd /_apt/ && \
    dpkg -i ./libssl-dev_1.0.1t-1+deb8u12_amd64.deb \
            ./libssl-doc_1.0.1t-1+deb8u12_all.deb \
            ./libssl1.0.0_1.0.1t-1+deb8u12_amd64.deb \
            ./openssl_1.0.1t-1+deb8u12_amd64.deb
RUN apt-mark hold libssl-dev libssl1.0 libssl-doc openssl

###

FROM openssl-ssl3 AS batman

WORKDIR /root

RUN apt-get update && apt-get install -y curl
COPY poodled.crt /usr/local/share/ca-certificates/poodled.crt
RUN update-ca-certificates

###

FROM openssl-ssl3 AS catwoman

WORKDIR /root

COPY poodled.crt /root/poodled.crt
COPY poodled.key /root/poodled.key

###

FROM debian AS joker

WORKDIR /root

RUN apt-get update && apt-get install -y python3-scapy python3-cryptography
COPY poodle.py .

FROM debian

WORKDIR /root

RUN apt-get update && apt-get install -y curl tcpdump

FROM debian AS poodlab
WORKDIR /root
RUN apt-get update && apt-get install -y curl tcpdump

FROM nginx AS catwoman
WORKDIR /root
RUN apt-get update && apt-get install -y iproute2

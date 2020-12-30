IP_BATMAN=$$(docker exec trinity hostname -i)
IP_CATWOMAN=$$(docker exec morpheus hostname -i)
IP_JOKER_INT=$$(docker exec smith hostname -i | cut -d ' ' -f 1)
IP_JOKER_PUB=$$(docker exec smith hostname -i | cut -d ' ' -f 2)
IP_NET_INT=$$(echo $(IP_JOKER_INT) | cut -d '.' -f 1,2,3).0/20
IP_NET_PUB=$$(echo $(IP_JOKER_PUB) | cut -d '.' -f 1,2,3).0/20

poodled.crt:
	openssl req -x509 -nodes -newkey rsa:2048 \
		-subj "/CN=morpheus" \
		-keyout ./poodled.key -out ./poodled.crt

prepare: poodled.crt clean
	docker build --target trinity --tag trinity .
	docker build --target morpheus --tag morpheus .
	docker build --target smith --tag smith .
	docker network create poodle_public_net
	docker network create poodle_private_net

morpheus:
	docker run \
		--cap-add NET_ADMIN \
		--network poodle_public_net \
		--hostname morpheus \
		--name morpheus \
		--rm --interactive --tty morpheus /bin/bash

smith:
	docker run \
		--network poodle_private_net \
		--hostname smith \
		--name smith \
		--rm --interactive --tty smith /bin/bash

trinity:
	docker run \
		--cap-add NET_ADMIN \
		--network poodle_private_net \
		--hostname trinity \
		--name trinity \
		--rm --interactive --tty trinity /bin/bash

network:
	docker network connect poodle_public_net smith
	docker exec trinity  ip route add $(IP_NET_PUB) via $(IP_JOKER_INT)
	docker exec morpheus ip route add $(IP_NET_INT) via $(IP_JOKER_PUB)
	docker exec trinity  sh -c "echo '$(IP_CATWOMAN) morpheus' >> /etc/hosts"
	docker exec morpheus sh -c "echo '$(IP_BATMAN)   trinity'   >> /etc/hosts"

clean:
	if docker ps | grep morpheus; then docker stop morpheus; fi
	if docker ps | grep trinity; then docker stop trinity; fi
	if docker ps | grep smith; then docker stop smith; fi
	if docker network ls | grep poodle > /dev/null; then \
		docker network remove poodle_public_net poodle_private_net; \
	fi
	if stat "poodled.*" 2> /dev/null; then rm poodled.key poodled.cert; fi

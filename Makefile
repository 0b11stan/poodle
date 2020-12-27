IP_BATMAN=$$(docker exec batman hostname -i)
IP_CATWOMAN=$$(docker exec catwoman hostname -i)
IP_JOKER_INT=$$(docker exec joker hostname -i | cut -d ' ' -f 1)
IP_JOKER_PUB=$$(docker exec joker hostname -i | cut -d ' ' -f 2)
IP_NET_INT=$$(echo $(IP_JOKER_INT) | cut -d '.' -f 1,2,3).0/20
IP_NET_PUB=$$(echo $(IP_JOKER_PUB) | cut -d '.' -f 1,2,3).0/20

prepare: clean
	openssl req -x509 -nodes -newkey rsa:2048 \
		-subj "/CN=catwoman" \
		-keyout ./poodled.key -out ./poodled.crt
	docker build --target poodlab --tag poodlab .
	docker build --target catwoman --tag catwoman .
	docker network create poodle_public_net
	docker network create poodle_private_net

catwoman:
	docker run \
		--cap-add NET_ADMIN \
		--network poodle_public_net \
		--hostname catwoman \
		--name catwoman \
		--rm --detach catwoman
	docker exec --interactive --tty catwoman /bin/bash

joker:
	docker run \
		--network poodle_private_net \
		--hostname joker \
		--name joker \
		--rm --interactive --tty poodlab /bin/bash

batman:
	docker run \
		--cap-add NET_ADMIN \
		--network poodle_private_net \
		--hostname batman \
		--name batman \
		--rm --interactive --tty poodlab /bin/bash

network:
	docker network connect poodle_public_net joker
	docker exec batman   ip route add $(IP_NET_PUB) via $(IP_JOKER_INT)
	docker exec catwoman ip route add $(IP_NET_INT) via $(IP_JOKER_PUB)
	docker exec batman   sh -c "echo '$(IP_CATWOMAN) catwoman' >> /etc/hosts"
	docker exec catwoman sh -c "echo '$(IP_BATMAN)   batman'   >> /etc/hosts"

clean:
	if docker ps | grep catwoman; then docker stop catwoman; fi
	if docker network ls | grep poodle > /dev/null; then \
		docker network remove poodle_public_net poodle_private_net; \
	fi
	if stat "poodled.*" 2> /dev/null; then rm poodled.key poodled.cert; fi

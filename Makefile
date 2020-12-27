prepare:
	docker build --tag catwoman ./catwoman/
	docker build --tag batman ./batman/
	docker build --tag joker ./joker/
	docker network create poodle_public_net
	docker network create poodle_private_net
	docker run \
		--network poodle_public_net \
    --hostname catwoman \
    --name catwoman \
    --rm --detach catwoman
	echo IP de catwoman: $$(docker exec catwoman hostname -i)

run_batman:
	docker run \
    --network poodle_private_net \
    --hostname batman \
    --name batman \
    --rm --interactive --tty batman /bin/bash

run_joker:
	docker run \
    --network poodle_private_net \
    --hostname joker \
    --name joker \
    --rm --interactive --tty joker /bin/bash
	docker network connect poodle_public_net joker

clean:
	docker stop catwoman
	docker network remove poodle_public_net
	docker network remove poodle_private_net

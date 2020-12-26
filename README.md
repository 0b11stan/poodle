# Proof of concept: POODLE

Ce dépôt contient une preuve d'exploitation de l'attaque **POODLE**. Cette
attaque permet de décrypter une communication chiffrée avec TLS. Elle s'appuie
sur un enchainement de plusieurs vulnérabilités qui touchent les serveurs web
dont la version de TLS est **inferieur à 1.3**.

Le fonctionnement de son POODLE est parfaitement illustré par son nom qui est
l'acronyme de "**P**adding **O**racle **O**n **D**owngraded **L**egacy
**E**ncryption".

Cette attaque fonctionne en 3 temps:
1. Mettre en place une attaque par homme du milieux au niveau réseau.
2. Forcer une version inferieur (SSLv3) de SSL/TLS sur le client.
3. On utilise la vuln Padding Oracle sur CBC pour découvrir du contenu (cookie).

## Lab

Build la machine de catwoman.
```bash
  docker build --tag catwoman ./catwoman/
```

Build la machine de batman.
```bash
  docker build --tag batman ./batman/
```

Build la machine du joker.
```bash
  docker build --tag joker ./joker/
```

Créer le réseau cible **poodle_private_net**.
```bash
  docker network create poodle_private_net
```

Créer un réseau publique **poodle_public_net**.
```bash
  docker network create poodle_public_net
```

Créer le serveur de catwoman et l'attacher au réseau publique.
```bash
  docker run \
    --network poodle_public_net \
    --hostname catwoman \
    --name catwoman \
    --rm --detach catwoman
```

Créer la machine de batman et l'attacher au réseau privé.
```bash
  docker run \
    --network poodle_private_net \
    --hostname batman \
    --name batman \
    --rm --interactive --tty batman /bin/bash
```

Créer la machine du joker et l'attacher au réseau privé.
```bash
  docker run \
    --network poodle_private_net \
    --hostname joker \
    --name joker \
    --rm --interactive --tty joker /bin/bash
```

Ajouter la machine du joker au réseau publique.
```bash
  docker network connect poodle_public_net joker
```

A ce stade batman ne devrait pas être en capacité de communiquer avec catwoman.
```
root@batman:/# ping -c 1 catwoman
ping: catwoman: Name or service not known
```

Mais devrait être capable de communiquer avec joker.
```
root@batman:/# ping -c 1 joker 
PING joker (172.21.0.2) 56(84) bytes of data.
64 bytes from joker.poodle_private_net (172.21.0.2): icmp_seq=1 ttl=64 time=0.094 ms

--- joker ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.094/0.094/0.094/0.000 ms
```

De son côté joker devrait être capable de communiquer avec batman.
```
root@joker:/# ping -c 1 batman
PING batman (172.21.0.3) 56(84) bytes of data.
64 bytes from batman.poodle_private_net (172.21.0.3): icmp_seq=1 ttl=64 time=0.118 ms

--- batman ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.118/0.118/0.118/0.000 ms
```

Mais puisqu'il à été ajouté au réseau publique, il peut aussi communiquer avec
catwoman.
```
root@joker:/# ping -c 1 catwoman
PING catwoman (172.20.0.2) 56(84) bytes of data.
64 bytes from catwoman.poodle_public_net (172.20.0.2): icmp_seq=1 ttl=64 time=0.164 ms

--- catwoman ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.164/0.164/0.164/0.000 ms
```

## Ressources

https://www.youtube.com/watch?v=BbwC8f_aBMQ

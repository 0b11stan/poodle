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
  docker build --tag robin ./catwoman/
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
    --name catwoman \
    --detach catwoman
```

Créer la machine de batman et l'attacher au réseau privé.
```bash
  docker run \
    --network poodle_private_net \
    --name batman \
    --interactive --tty batman /bin/bash
```

Créer la machine du joker et l'attacher au réseau privé.
```bash
  docker run \
    --network poodle_private_net \
    --name joker \
    --interactive --tty joker /bin/bash
```

Ajouter la machine du joker au réseau publique.
```bash
  docker network connect poodle_public_net joker
```

## Ressources

https://www.youtube.com/watch?v=BbwC8f_aBMQ

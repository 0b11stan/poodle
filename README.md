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

La commande `make prepare` permet de préparer l'environnement du laboratoire:

* Construit les machines de catwoman, batman et joker.
* Créé un réseaux privé et publique.
* Démarre le serveur de catwoman dans le réseau publique et affiche son IP.

En jouant `make run_batman` on démarre la machine de batman dans le réseau privé
et on accède à un shell à l'interieur de cette machine.

On peut vérifier que batman ne peut pas accéder à la machine de catwoman.
```
root@batman:~# ping -c 1 172.27.0.2
PING 172.27.0.2 (172.27.0.2) 56(84) bytes of data.

--- 172.27.0.2 ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms
```

En jouant `make run_joker` on démarre la machine du joker à l'intersection du
réseau privé et publique puis on accède à un shell à l'interieur de cette
machine.

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

Une fois toutes les opérations finies on peut réaliser un `make clean` pour
éteindre les machines et supprimer les réseaux créés.

## Ressources

https://www.youtube.com/watch?v=BbwC8f_aBMQ

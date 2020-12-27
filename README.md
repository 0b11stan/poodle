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

1. `make prepare`
2. `make catwoman`, `make joker`, `make batman`
3. `make network`

Joker:
```
root@joker:~# ping -c 1 catwoman | grep received
1 packets transmitted, 1 received, 0% packet loss, time 0ms
root@joker:~# ping -c 1 batman | grep received
1 packets transmitted, 1 received, 0% packet loss, time 0ms
```

Batman:
```
root@batman:~# ping -c 1 joker | grep received
1 packets transmitted, 1 received, 0% packet loss, time 0ms
root@batman:~# ping -c 1 catwoman | grep received
1 packets transmitted, 1 received, 0% packet loss, time 0ms
```

Catwoman:
```
root@catwoman:~# ping -c 1 joker | grep received
1 packets transmitted, 1 received, 0% packet loss, time 0ms
root@catwoman:~# ping -c 1 batman | grep received
1 packets transmitted, 1 received, 0% packet loss, time 0ms
```


Une fois toutes les opérations finies on peut réaliser un `make clean` pour
éteindre les machines et supprimer les réseaux créés.

## Ressources

https://www.youtube.com/watch?v=BbwC8f_aBMQ

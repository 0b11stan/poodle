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

Remarque: les ligne 19 et 20 de la configuration nginx sont intéressantes et
contiennent la vulnérabilité.
```
19  ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
20  ssl_prefer_server_ciphers on;
```

En supprimant la mention `SSLv3` de la ligne 19 on empêcherait l'attaque.

## Exploitation

Realiser une connection ssl en forcant la version 3:
```
root@catwoman:~# openssl s_server -ssl3 -key /root/poodled.key -cert /root/poodled.crt -accept 443 -www
root@batman:~# openssl s_client -ssl3 -connect catwoman:443
```

En utilisant les commandes ci-dessus on obtient le traffique SSL détaillé dans
[trace1.py](./trace1.py) qui passe par joker.

On peut aussi utiliser une commande curl classique qui, si on force le traffique
en sslv3 (`curl -3 https://catwoman`) va nous donner une trace sensiblement similaire ([trace2.py](./trace2.py)).

## Ressources

https://www.youtube.com/watch?v=BbwC8f_aBMQ

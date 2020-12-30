# Proof of concept: POODLE

Ce dépôt contient une preuve d'exploitation de l'attaque **POODLE**. Cette
attaque permet de décrypter une communication chiffrée avec TLS. Elle s'appuie
sur un enchainement de plusieurs vulnérabilités qui touchent les serveurs web
dont la version de TLS est **inferieur à 1.3**.

Le fonctionnement de POODLE est parfaitement illustré par son nom qui est
l'acronyme de "**P**adding **O**racle **O**n **D**owngraded **L**egacy
**E**ncryption". Lors d'une attaque par homme du milieux, l'attaquant peut
"voir" tout le traffique de sa victime. Ce type d'attaque est très fréquent et
facilité par de nombreuses vunérabilités au niveau des couches physiques et de
liaison de donnée. Ces vulnérabilité sont difficiles à corrigés prour des
raisons d'interopérabilité entre les réseaux à l'échelle d'internet. Ainsi,
cela fait maintenant plusieurs décénies que les concepteurs d'applications ne se
reposent plus sur les couches inferieurs pour assurer la confidentialité des
donnés échangés. Des protocoles de chiffrement comme SSL/TLS sont aujourd'hui
les seul rempare efficace contre les attaques par homme du milieux.

Aujourd'hui, l'enjeux pour un attaquant est donc de déjouer ces mechanismes de
chiffrement de niveau applicatif et c'est ici que POODLE intervient puisquelle
à pour objectif de permettre, par une attaque "en ligne", le dèchiffrement des
donnée encapsulés par le protocole TLS.

Cette attaque fonctionne souvent en 3 temps:
1. Mettre en place une attaque par homme du milieux au niveau réseau.
2. Dégrader le niveau de sécurité d'une connexion tls en forcant une version
   ancienne du protocole.
3. Utiliser une attaque de cryptanalyse (Padding Oracle) à laquelle la version
   dégradée est vulnérable pour découvrir un élément sensible.

## Preuve d'exploitation

### Le laboratoire

**TL;DR:**
* `make prepare` dans un premier terminal
* `make catwoman` dans un deuxième terminal
* `make joker` dans un troisième terminal
* `make batman` dans un quatrième terminal
* `make network` dans le premier terminal
* _be nasty_
* `make clean` une fois qu'on à fini de jouer pour tout supprimer

TODO : scénario

#### Construction des machines

`make prepare`

Remarque: les ligne 19 et 20 de la configuration nginx sont intéressantes et
contiennent la vulnérabilité.
```
19  ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
20  ssl_prefer_server_ciphers on;
```

En supprimant la mention `SSLv3` de la ligne 19 on empêcherait l'attaque.

#### Connection aux machines

`make catwoman`, `make joker`, `make batman`

#### Configurer les réseau

`make network`

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

#### Détruire le laboratoire et tout les méfais qu'il contient

`make clean`

### Exploitation

Realiser une connection ssl en forcant la version 3:
```
root@catwoman:~# openssl s_server -ssl3 -key /root/poodled.key -cert /root/poodled.crt -accept 443 -www
root@batman:~# openssl s_client -ssl3 -connect catwoman:443
```

En utilisant les commandes ci-dessus on obtient le traffique SSL détaillé dans
[trace1.py](./trace1.py) qui passe par joker.

On peut aussi utiliser une commande curl classique qui, si on force le traffique
en sslv3 (`curl -3 https://catwoman`) va nous donner une trace sensiblement similaire ([trace2.py](./trace2.py)).

On à du rebuild openssl pour autoriser l'utilisation de sslv3. Après ça le
downgrade fonctionne bien.

Sur la machine de catwoman on démarre un serveur qui refuse les protocoles > à
SSLv3 pour générer le traffique qui sera envoyer par notre attaquant et tester
que le downgrade foncitonne bien du côté du client.
```
root@catwoman:~# openssl s_server -key /root/poodled.key -cert /root/poodled.crt -accept 443 -www -no_tls1_2 -no_tls1_1 -no_tls1
Using default temp DH parameters
Using default temp ECDH parameters
ACCEPT
```

Sur la machine de batman on fait une requête mais cette fois sans forcer
l'utilisation de sslv3. On voit bien que pourtant c'est bien ce protocole qui
aura été utilisé pour la communication au final. Pour constater le changement de
protocole, se référer au fichier [trace10.py](./trace10.py) pour une lecture
au format text ou au fichier [legit_downgrade.pcap](./legit_downgrade.pcap) pour
le traffique réseau brute.
```
root@batman:~# openssl s_client -connect catwoman:443
CONNECTED(00000003)
depth=0 CN = catwoman
verify return:1
---
Certificate chain
 0 s:/CN=catwoman
   i:/CN=catwoman
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDBzCCAe+gAwIBAgIUUzUL9khTt2GxSYH7oUMz22pg6RkwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIY2F0d29tYW4wHhcNMjAxMjMwMDk0NzI1WhcNMjEwMTI5
MDk0NzI1WjATMREwDwYDVQQDDAhjYXR3b21hbjCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBAMWSyPZ6UDTxHhgGwAOzU39heX+Ub9mNqZA79MOqQQyzrr5x
sZ8yN4b9auK1MDsizuyMCn6qSuLwYQBOJ/WeBer5IdcdZTOZiiT+Dqh3nIp6LRQt
FNqZQ4Cth5g1a/8NLSQjmtc8I5saFoVcrcGZlo+oW7aSwNfseakHAYZBnoWQq3qc
AwmE7C5NYZzXMvWws8sT6ULHzfDJ4A2ajjGQRgeOQRPLxxp9BeVrTe0+GHkPXmsA
9N9va/or9OsCELjLDc0ZdDRvzDGIMmL26wWoYi68+HLNZzu9LTuJN3agTzU/kCL7
G8sXzS40KEHzhv1cYbuG652msdcA8fp+PBSacVMCAwEAAaNTMFEwHQYDVR0OBBYE
FOfdv6hxsQgFeuKal8b78c3CLpvsMB8GA1UdIwQYMBaAFOfdv6hxsQgFeuKal8b7
8c3CLpvsMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAJmm13wN
LstDmaqpHMzkZk7To758U/XPE7PGRefg9BonagVMzkY40k4FC8rm/XvvSCSblXqE
Ik8gcHOe+7jtF8s24Dywj0eq4J89IpEIyq4b6CYEBhBTsqKCdOQWa13uXOCkiTXa
NPRbgX7nMFFF88iMbXFsR+t5wka+t08/nuJd9V6gSSo9U3mAKzHBGStxTRztfW+k
Nu9PBdSEygQgv3jttgKXWV3rSn0JytFOiVIT/9OKdlnHwLaHBe9AXESboJ2KkdkE
llc6QASPp+jprWpKLm4hIEvmZtR1Gk+GOy3W8P+XcPfakK/x2Yb2yu3rKIJRm/ge
7zY5koBKIhXU4es=
-----END CERTIFICATE-----
subject=/CN=catwoman
issuer=/CN=catwoman
---
No client certificate CA names sent
---
SSL handshake has read 1313 bytes and written 439 bytes
---
New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-SHA
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : SSLv3
    Cipher    : ECDHE-RSA-AES256-SHA
    Session-ID: 24B3C1DFE52D4CA8200A205036020786E34F1DD3D9EE95770FCA10F7F13BA20C
    Session-ID-ctx: 
    Master-Key: D69C0F2492859CEECEAB6CA3486C91324EDC716181B9D6E1A31F144C31C926CD30EFAA9943004DE26804FC64619A0BA6
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1609353992
    Timeout   : 300 (sec)
    Verify return code: 0 (ok)
---
```

Pour exploiter il suffit d'intercepter le "Client Hello" de batman, de changer
le protocole par sslv3, le serveur va alors renvoyer un "Server Hello" pour
sslv3 et le client reverra ses ambitions cryptographiques à la baisse comme dans
l'exemple précédent.

## Mitigation

Cette attaque fut extrêmement sensible et d'une efficacité redoutable. Les
réponses ont été multiples pour corriger la vulnérabilité et des efforts de la
communauté à tout les niveau ont permit une sécurité en profondeur qui rend
cette attaque de moins en moins probable sur la grande majorité des applications:

* Les dévellopeurs de serveur web (apache, nginx, ...) ont ajouté des options
  permettant de choisir au moyens d'une liste blanche les versions de TLS que
  leur produit pourrait accepter obligeant les gens à spécifier explicitement
  le niveau de sécurité de leurs serveurs en fonction du niveau
  d'intéropérabilité nécessaire.
* Les dévellopeurs de client web (curl, firefox, chrome, ...) ont durcie les
  options par défaut, ajoutant la possibilité de limiter l'étandue des versions
  accepté et affichant souvent des messages d'avertissement lorsqu'un protocole
  particulièrement vieux est utilisé.
* Les dévellopeurs des librairies de cryptographie (openssl, libressl, ...), sur
  lesquelles les programmes cités auparavant s'appuient, ont souvent déprécié
  les protocoles en question au sein même du code source, obligeant une
  reconstruction des librairies pour utiliser les versions vulnérables du
  protocole.

## Achivements

- [x] simulter un réseau MITM avec docker
- [x] sniffer le traffique ssl/tls avec scapy
- [x] downgrade les version pour pouvoir faire du sslv3
- [x] désactiver les sécurité pour rendre le labo vulnérables
- [x] générer un traffique vulnérable avec openssl
- [ ] dev un script capable de modifier le traffique ssl/tls avec scapy
- [ ] utiliser le script pour réaliser un downgrade de version de tls
- [ ] implémenter l'attaque padding oracle sur AES CBC

## Ressources

* [SSLv3 Poodle Vulnerability | Password theft](https://www.youtube.com/watch?v=BbwC8f_aBMQ)
* [Downgrade OpenSSL to support SSLv3](https://devcondition.com/article/debian-10-downgrade-openssl/)
* [Exploiting The SSL 3.0 Fallback](./ssl-poodle.pdf)
* [Testing TLS_FALLBACK_SCSV](https://dwradcliffe.com/2014/10/16/testing-tls-fallback.html)

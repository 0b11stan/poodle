##
# Client refuses tls 1.2, tls 1.1 and tls 1.0 with openssl
#   morpheus : openssl s_server -key /...key -cert /...crt -accept 443 -www
#   trinity : openssl s_client -connect morpheus:443 \
#               -no_tls1_2 -no_tls1_1 -no_tls1
#   smith : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())
##

###[ TCP ]### 
  sport= 42134
  dport= https
  seq= 596964978
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x5859
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (2277548314, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 42134
  seq= 1459475212
  ack= 596964979
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x5859
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3126222250, 2277548314)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 42134
  dport= https
  seq= 596964979
  ack= 1459475213
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277548314, 3126222250))]

###[ TCP ]### 
  sport= 42134
  dport= https
  seq= 596964979
  ack= 1459475213
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x58cb
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277548314, 3126222250))]
###[ TLS ]### 
     type= handshake
     version= SSLv3
     len= 117
     iv= b''
     \msg\
      |###[ TLS Handshake - Client Hello ]### 
      |  msgtype= client_hello
      |  msglen= 113
      |  version= SSLv3
      |  gmt_unix_time= Fri, 10 Nov 2034 17:09:05 +0000 (2046791345)
      |  random_bytes= 11fe6e7ba0a3dfdb8c48902b3b586e23d37110ddb06cac0168d9ee26
      |  sidlen= 0
      |  sid= ''
      |  cipherslen= 74
      |  ciphers= [TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_AES_256_CBC_SHA, TLS_DHE_DSS_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDH_RSA_WITH_AES_256_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_SEED_CBC_SHA, TLS_DHE_DSS_WITH_SEED_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDH_RSA_WITH_AES_128_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_SEED_CBC_SHA, TLS_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDHE_RSA_WITH_RC4_128_SHA, TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, TLS_ECDH_RSA_WITH_RC4_128_SHA, TLS_ECDH_ECDSA_WITH_RC4_128_SHA, TLS_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_RC4_128_MD5, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_EMPTY_RENEGOTIATION_INFO_SCSV]
      |  complen= 1
      |  comp= null
      |  extlen= None
      |  ext= None
     mac= b''
     pad= b''
     padlen= None

###[ TCP ]### 
  sport= https
  dport= 42134
  seq= 1459475213
  ack= 596965101
  dataofs= 8
  reserved= 0
  flags= A
  window= 509
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126222250, 2277548314))]

###[ TCP ]### 
  sport= https
  dport= 42134
  seq= 1459475213
  ack= 596965101
  dataofs= 8
  reserved= 0
  flags= PA
  window= 509
  chksum= 0x5d1a
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126222254, 2277548314))]
###[ TLS ]### 
     type= handshake
     version= SSLv3
     len= 81
     iv= b''
     \msg\
      |###[ TLS Handshake - Server Hello ]### 
      |  msgtype= server_hello
      |  msglen= 77
      |  version= SSLv3
      |  gmt_unix_time= Sun, 24 Aug 2104 21:04:49 +0000 (4249055089)
      |  random_bytes= 86e08878dcf73cfba886c8854a557e87ef589523797758d467991ccf
      |  sidlen= 32
      |  sid= '\xea\x1d\xb6\xc1\xab\xc9q\x8fk\x90\x7fkg\xe5F\xa3\xbb*j\xe1\x99\x80\xe0\x91V\xb7.\x8bK\x97\xc7U'
      |  cipher= TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
      |  comp= null
      |  extlen= 5
      |  \ext\
      |   |###[ TLS Extension - Renegotiation Indication ]### 
      |   |  type= renegotiation_info
      |   |  len= 1
      |   |  reneg_conn_len= 0
      |   |  renegotiated_connection= ''
     mac= b''
     pad= b''
     padlen= None
###[ TLS ]### 
        type= handshake
        version= SSLv3
        len= 789
        iv= b''
        \msg\
         |###[ TLS Handshake - Certificate ]### 
         |  msgtype= certificate
         |  msglen= 785
         |  certslen= 782
         |  certs= [(779, [X.509 Cert. Subject:/CN=catwoman, Issuer:/CN=catwoman])]
        mac= b''
        pad= b''
        padlen= None
###[ TLS ]### 
           type= handshake
           version= SSLv3
           len= 331
           iv= b''
           \msg\
            |###[ TLS Handshake - Server Key Exchange ]### 
            |  msgtype= server_key_exchange
            |  msglen= 327
            |  \params\
            |   |###[ Server ECDH parameters - Named Curve ]### 
            |   |  curve_type= named_curve
            |   |  named_curve= secp256r1
            |   |  pointlen= 65
            |   |  point= '\x043\xa32j\x07eI\xc5]\xc2\xba\xb8v\xec\xb5\x1e\x16^\xc5\x9e\xe3\x87\xbeM\xa3\xef\xc0\x92\x17_4\x7f<\xbcG\x91\xc7Nd^;\xa3m\x19o\xce\xa7O\x07\xaa\xb6S\xcb\x7f\xf1\xad\xe2\xdcP \x9fK\xeb\xcb'
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= 'r\xad.\xd1\x83\x7f\xd5\'N\x83\xc0t\x92\xe9zE\xac\xcc\x0f\xd4\x1a\xff\xc6".a\x98\x9fP\x04\xb31\x9fwCn\t\xd5N^1\x9ex\xdf\xbb\xb4\x8a\xa1Zgg\x8f\x0c\xb2V\xa9\x89\x97\xbc\x90Y\xb4\x8f\x02\xa9\xe5\x8eM\xf1\x88]N2\x7f\x96\xd4s"\x15\x18\xdc\xd5\xf1\xb3\xe76\xb5\xaa:\xfa&g}\xee\x87`\x05\x89O,&\xa7d\x0el\xa4\x92\xd5Ui\x8e\xc8;\'vFql</\xc2\xe5\x8a\xeaF\xe2\x1f\x88{&\xe8\xe2\x01\xe1h\xc5\xda\xda\x9d\xdd\xa5\x03\xbe\x8d)\xa1|l\x0c\x82xD\x9fOj\x1f\xa8\xabNp`gp\rB\xa7H\xa7z\x99\xc6\xa9\xe2&\x90\xbd\xab\x9a\x96y\xd2R-\x92\xf3\x17\xabj\x942P\xe0\xb5\x10[\xb4\r\xa3\xf9\x0f\x8d"\xf8$\x99\x9as\xfb\xbe\xb1K\x06\xbf!\x0e\x16\xbb\xf6G0\x1fm\'\xcb\xb5\xc1\t\x07\xca/ \x0b\xce\xa9\x0cx1~$\xed\xc8\xee?\r\x9af\x99\xdaCr\xde\x82\x9f4\x16A'
           mac= b''
           pad= b''
           padlen= None
###[ TLS ]### 
              type= handshake
              version= SSLv3
              len= 4
              iv= b''
              \msg\
               |###[ TLS Handshake - Server Hello Done ]### 
               |  msgtype= server_hello_done
               |  msglen= 0
              mac= b''
              pad= b''
              padlen= None

###[ TCP ]### 
  sport= 42134
  dport= https
  seq= 596965101
  ack= 1459476438
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277548318, 3126222254))]

###[ TCP ]### 
  sport= 42134
  dport= https
  seq= 596965101
  ack= 1459476438
  dataofs= 8
  reserved= 0
  flags= PA
  window= 501
  chksum= 0x58e7
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277548320, 3126222254))]
###[ TLS ]### 
     type= handshake
     version= SSLv3
     len= 70
     iv= b''
     \msg\
      |###[ TLS Handshake - Client Key Exchange ]### 
      |  msgtype= client_key_exchange
      |  msglen= 66
      |  \exchkeys\
      |   |###[ Raw ]### 
      |   |  load= 'A\x04=\xae\xd9$rAga\x90\x8d\xd3hO\xcf\xb9k\xe234d\xb1\xc1j\x80!\x7f\x03\x97\xe0a\xb5\x06C\x1aJ~ga\xfd#onlB\x94\x00\xff\xf3\x01\x1c+\xf4\x04@\x93\x12Z\xff\xbf\x01\x0c\xa4\xd6*'
     mac= b''
     pad= b''
     padlen= None
###[ TLS ]### 
        type= change_cipher_spec
        version= SSLv3
        len= 1
        iv= b''
        \msg\
         |###[ TLS ChangeCipherSpec ]### 
         |  msgtype= change_cipher_spec
        mac= b''
        pad= b''
        padlen= None
###[ TLS ]### 
           type= handshake
           version= SSLv3
           len= 64
           iv= b''
           \msg\
            |###[ Raw ]### 
            |  load= "\xa0\xb2\xeaD\xcfN\xba\x8e\x7f\xd8\xe1\xe2&'d\rv\x19\x9eBc\xde`\xd0\x14\xda\x05\t\xab\xe4`\xfb\xcb\x91A\x16\xf5\x9dty\xd2\xa2[\x08\x0b0\x98\xeb\xb4\x89\xe5[MH\xe8%\xf6S\x99\xa5bn\xd2\xb0"
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= https
  dport= 42134
  seq= 1459476438
  ack= 596965251
  dataofs= 8
  reserved= 0
  flags= A
  window= 508
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126222256, 2277548320))]

###[ TCP ]### 
  sport= https
  dport= 42134
  seq= 1459476438
  ack= 596965251
  dataofs= 8
  reserved= 0
  flags= PA
  window= 508
  chksum= 0x589c
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126222256, 2277548320))]
###[ TLS ]### 
     type= change_cipher_spec
     version= SSLv3
     len= 1
     iv= b''
     \msg\
      |###[ TLS ChangeCipherSpec ]### 
      |  msgtype= change_cipher_spec
     mac= b''
     pad= b''
     padlen= None
###[ TLS ]### 
        type= handshake
        version= SSLv3
        len= 64
        iv= b''
        \msg\
         |###[ Raw ]### 
         |  load= '\xbc\xb1fc\xaf\x06o\xaf\x81|[\x8e\x90t\xb3\x080\x02\xb8\xf0R\x8c}\xf4lqczF1n\x19h\xdcb\x05H\x93b\\\xa5\xffP\xe9\x14\xfa\x98\\\xb0U6\xcf\x9dC\xe6F\xda\xaf\xfcRMX\xddE'
        mac= b''
        pad= b''
        padlen= None

###[ TCP ]### 
  sport= 42134
  dport= https
  seq= 596965251
  ack= 1459476513
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277548320, 3126222256))]

###[ TCP ]### 
  sport= 42134
  dport= https
  seq= 596965251
  ack= 1459476513
  dataofs= 8
  reserved= 0
  flags= FA
  window= 501
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277550225, 3126222256))]

###[ TCP ]### 
  sport= https
  dport= 42134
  seq= 1459476513
  ack= 596965252
  dataofs= 8
  reserved= 0
  flags= FA
  window= 508
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126224161, 2277550225))]

###[ TCP ]### 
  sport= 42134
  dport= https
  seq= 596965252
  ack= 1459476514
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277550225, 3126224161))]

<Sniffed: TCP:14 UDP:0 ICMP:0 Other:0>

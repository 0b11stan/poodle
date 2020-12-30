# client force ssl 3 with curl

# catwoman : openssl s_server -key /...key -cert /...crt -accept 443 -www
# batman : curl -3 https://catwoman
# joker : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())

###[ TCP ]### 
  sport= 50716
  dport= https
  seq= 293836672
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (1397308543, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 50716
  seq= 2871915582
  ack= 293836673
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (548107296, 1397308543)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 50716
  dport= https
  seq= 293836673
  ack= 2871915583
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1397308543, 548107296))]

###[ TCP ]### 
  sport= 50716
  dport= https
  seq= 293836673
  ack= 2871915583
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x11ec
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1397308544, 548107296))]
###[ TLS ]### 
     type= handshake
     version= SSLv3
     len= 105
     iv= b''
     \msg\
      |###[ TLS Handshake - Client Hello ]### 
      |  msgtype= client_hello
      |  msglen= 101
      |  version= SSLv3
      |  gmt_unix_time= Sun, 04 Sep 2005 07:25:43 +0000 (1125818743)
      |  random_bytes= 25195fa4ef8cb4bd08060ead35ea5cb1ffc36fc4d3613662e6e9a50d
      |  sidlen= 0
      |  sid= ''
      |  cipherslen= 62
      |  ciphers= [TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_AES_256_CBC_SHA, TLS_DHE_DSS_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDH_RSA_WITH_AES_256_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_SEED_CBC_SHA, TLS_DHE_DSS_WITH_SEED_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDH_RSA_WITH_AES_128_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_SEED_CBC_SHA, TLS_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_EMPTY_RENEGOTIATION_INFO_SCSV]
      |  complen= 1
      |  comp= null
      |  extlen= None
      |  ext= None
     mac= b''
     pad= b''
     padlen= None

###[ TCP ]### 
  sport= https
  dport= 50716
  seq= 2871915583
  ack= 293836783
  dataofs= 8
  reserved= 0
  flags= A
  window= 509
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (548107297, 1397308544))]

###[ TCP ]### 
  sport= https
  dport= 50716
  seq= 2871915583
  ack= 293836783
  dataofs= 8
  reserved= 0
  flags= FA
  window= 509
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (548107297, 1397308544))]

###[ TCP ]### 
  sport= https
  dport= 50716
  seq= 2871915584
  ack= 293836783
  dataofs= 8
  reserved= 0
  flags= RA
  window= 509
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (548107297, 1397308544))]

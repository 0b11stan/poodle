# client refuses tls 1.2 and tls 1.1 with openssl

# morpheus : openssl s_server -key /...key -cert /...crt -accept 443 -www
# trinity : openssl s_client -connect morpheus:443 -no_tls1_2 -no_tls1_1
# smith : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())

###[ TCP ]### 
  sport= 53834
  dport= https
  seq= 1915640572
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (1398833242, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 53834
  seq= 4090994703
  ack= 1915640573
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (549631995, 1398833242)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 53834
  dport= https
  seq= 1915640573
  ack= 4090994704
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1398833242, 549631995))]

###[ TCP ]### 
  sport= 53834
  dport= https
  seq= 1915640573
  ack= 4090994704
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x1243
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1398833242, 549631995))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.0
     len= 192
     iv= b''
     \msg\
      |###[ TLS Handshake - Client Hello ]### 
      |  msgtype= client_hello
      |  msglen= 188
      |  version= TLS 1.0
      |  gmt_unix_time= Fri, 22 May 2082 04:24:11 +0000 (3546649451)
      |  random_bytes= 7d1766eb874eac5bcaab310371b8cd9403979f064e064bce98a75915
      |  sidlen= 0
      |  sid= ''
      |  cipherslen= 74
      |  ciphers= [TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_AES_256_CBC_SHA, TLS_DHE_DSS_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDH_RSA_WITH_AES_256_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_SEED_CBC_SHA, TLS_DHE_DSS_WITH_SEED_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDH_RSA_WITH_AES_128_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_SEED_CBC_SHA, TLS_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDHE_RSA_WITH_RC4_128_SHA, TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, TLS_ECDH_RSA_WITH_RC4_128_SHA, TLS_ECDH_ECDSA_WITH_RC4_128_SHA, TLS_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_RC4_128_MD5, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_EMPTY_RENEGOTIATION_INFO_SCSV]
      |  complen= 1
      |  comp= null
      |  extlen= 73
      |  \ext\
      |   |###[ TLS Extension - Supported Point Format ]### 
      |   |  type= ec_point_formats
      |   |  len= 4
      |   |  ecpllen= 3
      |   |  ecpl= [uncompressed, ansiX962_compressed_prime, ansiX962_compressed_char2]
      |   |###[ TLS Extension - Supported Groups ]### 
      |   |  type= supported_groups
      |   |  len= 52
      |   |  groupslen= 50
      |   |  groups= [sect571r1, sect571k1, secp521r1, sect409k1, sect409r1, secp384r1, sect283k1, sect283r1, secp256k1, secp256r1, sect239k1, sect233k1, sect233r1, secp224k1, secp224r1, sect193r1, sect193r2, secp192k1, secp192r1, sect163k1, sect163r1, sect163r2, secp160k1, secp160r1, secp160r2]
      |   |###[ TLS Extension - Session Ticket ]### 
      |   |  type= session_ticket
      |   |  len= 0
      |   |  ticket= ''
      |   |###[ TLS Extension - Heartbeat ]### 
      |   |  type= heartbeat
      |   |  len= 1
      |   |  heartbeat_mode= peer_allowed_to_send
     mac= b''
     pad= b''
     padlen= None

###[ TCP ]### 
  sport= https
  dport= 53834
  seq= 4090994704
  ack= 1915640770
  dataofs= 8
  reserved= 0
  flags= A
  window= 508
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (549631995, 1398833242))]

  pubnum = import_point(curve, self.point)
###[ TCP ]### 
  sport= https
  dport= 53834
  seq= 4090994704
  ack= 1915640770
  dataofs= 8
  reserved= 0
  flags= PA
  window= 508
  chksum= 0x1638
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (549631997, 1398833242))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.0
     len= 66
     iv= b''
     \msg\
      |###[ TLS Handshake - Server Hello ]### 
      |  msgtype= server_hello
      |  msglen= 62
      |  version= TLS 1.0
      |  gmt_unix_time= Sun, 15 Jun 2064 08:55:40 +0000 (2980745740)
      |  random_bytes= 49039c29ce9a7f3e0f7014413fe02c06ea23cb9ec6378232323da7f3
      |  sidlen= 0
      |  sid= ''
      |  cipher= TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
      |  comp= null
      |  extlen= 22
      |  \ext\
      |   |###[ TLS Extension - Renegotiation Indication ]### 
      |   |  type= renegotiation_info
      |   |  len= 1
      |   |  reneg_conn_len= 0
      |   |  renegotiated_connection= ''
      |   |###[ TLS Extension - Supported Point Format ]### 
      |   |  type= ec_point_formats
      |   |  len= 4
      |   |  ecpllen= 3
      |   |  ecpl= [uncompressed, ansiX962_compressed_prime, ansiX962_compressed_char2]
      |   |###[ TLS Extension - Session Ticket ]### 
      |   |  type= session_ticket
      |   |  len= 0
      |   |  ticket= ''
      |   |###[ TLS Extension - Heartbeat ]### 
      |   |  type= heartbeat
      |   |  len= 1
      |   |  heartbeat_mode= peer_allowed_to_send
     mac= b''
     pad= b''
     padlen= None
###[ TLS ]### 
        type= handshake
        version= TLS 1.0
        len= 789
        iv= b''
        \msg\
         |###[ TLS Handshake - Certificate ]### 
         |  msgtype= certificate
         |  msglen= 785
         |  certslen= 782
         |  certs= [(779, [X.509 Cert. Subject:/CN=morpheus, Issuer:/CN=morpheus])]
        mac= b''
        pad= b''
        padlen= None
###[ TLS ]### 
           type= handshake
           version= TLS 1.0
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
            |   |  point= "\x04\xed\xcd|'\x96\xaa\r\x18\xa8\xfa\x99\xcbI\xd5v\xc5n~K\xee\xc9\x8d\xaeUc\x1f\x17?%-\x16\xe5\xab\xc9;vD\x8e\xe0!\x06\xf2\xfe\x87ns\x89\x1e-F7w\x0e\xb4\xacO\xab\xdeKn\x89n\xc0\xa3"
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= '\xa2BaC\x0f\xb2\x04rj\x90N\xcb\x99\xe3*7\x93\xdf\xdd^j\xcdW\x83\xc1\xd3\xc8\xd5\x92\xd3\xa6\xf8\x10\xae\':?\xad\x12V\xb6\xb7j\x97\x11\x13t\xfb\xa7\xeb\xd0\x94tl6Ao;\xfd\xa82\xf9\x86\x85\x8ae\x9f\xeb\xdeC\\\x0c\x06CN\x92\xa9T\xf4\x87d6\xf0\xea\xbb!\xbd\xa8\xed\xc3\xf3\xa0\xaf\xda\xd5N\x05Iz\x82f\xc5\xb1\xf0\x1f\xbc\xf8fS\xc0\xa0O9\xd2\x97\xc6\xce\x1a\x1e\x0fI\xf7\xe8$\x9b\xcb\x9cd\xccX\r\n}Q\xde\x1aI\xda\x8a\xa7B\x8dr\x99\x95\xf3y.\xc4g\xf4"\xe2M\xda$;0\xa3\xa2\xfe\x9e\x00i\xd5\xdb\xd1\xad\x1d\x16\x92E\x0e\x9f \xcf(\xd4\xc5 U??\xd6a\x02@i>\xdfQ2\x9ay\xaaM\xf7\xe2Q8\xfe\xd8\xa0\xb4\xa75\x0b\xa7\xbfl\xc9Lo\x1f\xfc\xae\xa2\xc5\x10\x8a\x85\x0f\\\xd8\xd0\x03\xab\xf6\x8d\x16\xa8%\xa2\x9bIv\xa6\x02\xf8l\x9e\xa1\xb3\xd7\xeb\xee}\xf0\x9bi\xc3\x10\xd6\x1buy'
           mac= b''
           pad= b''
           padlen= None
###[ TLS ]### 
              type= handshake
              version= TLS 1.0
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
  sport= 53834
  dport= https
  seq= 1915640770
  ack= 4090995914
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1398833244, 549631997))]

###[ TCP ]### 
  sport= 53834
  dport= https
  seq= 1915640770
  ack= 4090995914
  dataofs= 8
  reserved= 0
  flags= PA
  window= 501
  chksum= 0x1204
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1398833245, 549631997))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.0
     len= 70
     iv= b''
     \msg\
      |###[ TLS Handshake - Client Key Exchange ]### 
      |  msgtype= client_key_exchange
      |  msglen= 66
      |  \exchkeys\
      |   |###[ Raw ]### 
      |   |  load= 'A\x04\xa7G\x9d\xeb\xf5\xc4lJ\x80\xa6\x10\x06\xecQ\xf21nie\x93G9\xa3\x17~\xa5\xde\x12\x82Z\x9f\xb5R\xf0\x96\xd4\xe6F\x0b\xe5\x9d\xa9]2\x8f^@\x1c\xe6\xaa:\xd1\xe8\x92Z\x1cnS\xcb\xa0\x9c\xf3\xde\xae'
     mac= b''
     pad= b''
     padlen= None
###[ TLS ]### 
        type= change_cipher_spec
        version= TLS 1.0
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
           version= TLS 1.0
           len= 48
           iv= b''
           \msg\
            |###[ Raw ]### 
            |  load= "\xe0Q\x08\xc7\xd0a\x14|\x90\xb5\xc7\xd2\x147\xb2E\x9e\xa5\xf8\x06q\x82N\xf9\xb1\xe0BDB#\x93\x11r\xcct\xad'\xe6\x96tY#jD\xff\x8c\xc9\xa1"
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= https
  dport= 53834
  seq= 4090995914
  ack= 1915640904
  dataofs= 8
  reserved= 0
  flags= A
  window= 507
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (549631998, 1398833245))]

###[ TCP ]### 
  sport= https
  dport= 53834
  seq= 4090995914
  ack= 1915640904
  dataofs= 8
  reserved= 0
  flags= PA
  window= 507
  chksum= 0x1268
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (549631998, 1398833245))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.0
     len= 170
     iv= b''
     \msg\
      |###[ Raw ]### 
      |  load= '\x04\x00\x00\xa6\x00\x00\x01,\x00\xa0\xe0\x97t\xcc\x82\x19\x1a`\xdcx\xae\xab\xbc\xdai\xa1a`3UKS<:\x96\x04\x85u\xf7u\x0f\xa4\xab\xb20\xa2{\x04\xbf\x0cN\xb0\x13K\x8b\xb5\xd5\xe9\xb3T\xb7\xac\x19\x1f\xde\xdd\xbf-\x121\x85\x02\x11\xee~\xf0\x9b\xf1\x00x^\x146\xcb\xf7\x93\xac\n\xbd\xff\x1bC\xf5G\xb4j\xc6\xd9\xc4\xebeq\xf2\x1aN\x9c\xffr\x04\xad\xa1dl^\xa7%\xcf\x87\x07\xa1\x8e\x1et,\x91\xa8\xe7\xc0\xa1\xdb\x13@A\xfe\xea\xd2\x01\xa0\xd4pc!r\xea1\xce)\x83p\xa8\x04.(\xb8\xacS\xdf{\x06\xf4f\xf9\xe5v<\x15\xda\x0cH\x89'
     mac= b''
     pad= b''
     padlen= None
###[ TLS ]### 
        type= change_cipher_spec
        version= TLS 1.0
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
           version= TLS 1.0
           len= 48
           iv= b''
           \msg\
            |###[ Raw ]### 
            |  load= '\xe4\xc8\x08s\x96\x88\xd1\x9d\x86\xc5+\xc3\x1fds\xf91\n\xcfB\x1bEb\x14Q\r.\xb1\xd4O\xd3\x96\xe8~\x8c@\xcd%\x88v\xcd5\x10\x9e\xab\x9f\xf43'
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= 53834
  dport= https
  seq= 1915640904
  ack= 4090996148
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1398833245, 549631998))]

###[ TCP ]### 
  sport= 53834
  dport= https
  seq= 1915640904
  ack= 4090996148
  dataofs= 8
  reserved= 0
  flags= FA
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1398834951, 549631998))]

###[ TCP ]### 
  sport= https
  dport= 53834
  seq= 4090996148
  ack= 1915640905
  dataofs= 8
  reserved= 0
  flags= FA
  window= 507
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (549633704, 1398834951))]

###[ TCP ]### 
  sport= 53834
  dport= https
  seq= 1915640905
  ack= 4090996149
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1398834951, 549633704))]

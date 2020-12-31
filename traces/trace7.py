# server refuse tls 1.2 and tls 1.1 with openssl

# morpheus : openssl s_server -key /...key -cert /...crt -accept 443 -www \
#              -no_tls1_2 -no_tls1_1
# trinity : openssl s_client -connect morpheus:443
# smith : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())

>>> sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())
###[ TCP ]### 
  sport= 41238
  dport= https
  seq= 3396076080
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x585c
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3047691965, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 41238
  seq= 1206566918
  ack= 3396076081
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x585c
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3979380705, 3047691965)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 41238
  dport= https
  seq= 3396076081
  ack= 1206566919
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3047691965, 3979380705))]

###[ TCP ]### 
  sport= 41238
  dport= https
  seq= 3396076081
  ack= 1206566919
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x5975
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3047691965, 3979380705))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.0
     len= 284
     iv= b''
     \msg\
      |###[ TLS Handshake - Client Hello ]### 
      |  msgtype= client_hello
      |  msglen= 280
      |  version= TLS 1.2
      |  gmt_unix_time= Sat, 09 Aug 2087 12:48:43 +0000 (3711271723)
      |  random_bytes= 0d280c3d8993f9fdad554f487e92af73dd1c3fa45f1ece27f6d2569b
      |  sidlen= 0
      |  sid= ''
      |  cipherslen= 130
      |  ciphers= [TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_DHE_DSS_WITH_AES_256_GCM_SHA384, TLS_DHE_RSA_WITH_AES_256_GCM_SHA384, TLS_DHE_RSA_WITH_AES_256_CBC_SHA256, TLS_DHE_DSS_WITH_AES_256_CBC_SHA256, TLS_DHE_RSA_WITH_AES_256_CBC_SHA, TLS_DHE_DSS_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384, TLS_ECDH_RSA_WITH_AES_256_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_GCM_SHA256, TLS_DHE_RSA_WITH_AES_128_GCM_SHA256, TLS_DHE_RSA_WITH_AES_128_CBC_SHA256, TLS_DHE_DSS_WITH_AES_128_CBC_SHA256, TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_SEED_CBC_SHA, TLS_DHE_DSS_WITH_SEED_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDH_RSA_WITH_AES_128_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_SEED_CBC_SHA, TLS_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDHE_RSA_WITH_RC4_128_SHA, TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, TLS_ECDH_RSA_WITH_RC4_128_SHA, TLS_ECDH_ECDSA_WITH_RC4_128_SHA, TLS_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_RC4_128_MD5, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_EMPTY_RENEGOTIATION_INFO_SCSV]
      |  complen= 1
      |  comp= null
      |  extlen= 109
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
      |   |###[ TLS Extension - Signature Algorithms ]### 
      |   |  type= signature_algorithms
      |   |  len= 32
      |   |  sig_algs_len= 30
      |   |  sig_algs= [sha512+rsa, sha512+dsa, sha512+ecdsa, sha384+rsa, sha384+dsa, sha384+ecdsa, sha256+rsa, sha256+dsa, sha256+ecdsa, sha224+rsa, sha224+dsa, sha224+ecdsa, sha1+rsa, sha1+dsa, sha1+ecdsa]
      |   |###[ TLS Extension - Heartbeat ]### 
      |   |  type= heartbeat
      |   |  len= 1
      |   |  heartbeat_mode= peer_allowed_to_send
     mac= b''
     pad= b''
     padlen= None

###[ TCP ]### 
  sport= https
  dport= 41238
  seq= 1206566919
  ack= 3396076370
  dataofs= 8
  reserved= 0
  flags= A
  window= 507
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3979380705, 3047691965))]

/usr/lib/python3/dist-packages/scapy/layers/tls/keyexchange.py:588: CryptographyDeprecationWarning: Support for unsafe construction of public numbers from encoded data will be removed in a future version. Please use EllipticCurvePublicKey.from_encoded_point
  pubnum = import_point(curve, self.point)
###[ TCP ]### 
  sport= https
  dport= 41238
  seq= 1206566919
  ack= 3396076370
  dataofs= 8
  reserved= 0
  flags= PA
  window= 507
  chksum= 0x5d0e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3979380706, 3047691965))]
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
      |  gmt_unix_time= Mon, 01 May 1972 11:02:09 +0000 (73566129)
      |  random_bytes= 0bfdee13a50fd1cd184550a9e16da2fc1e034f76cbf7cb984807e660
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
            |   |  point= '\x04\xfe\x941\x88\x8c\x8f\xcb\x1a:9/wy\xae\xe4\xbc\x18\xa2l:\xde/\xf3\t3\x89w\x9f\xf4\xee\x12\x05\t\xb2t\xaa\xcc\x0b\xd88\x9b\x91\x0f\x8d\xc4`\x02\xfaAU\xf4e\xd5\x81\x84\xb1\x89\xe9\x93\x89#\x8eE\x1a'
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= "\x94\x99\xa2\x9b\x95\xb8\xfb\xad\xbce\x15s\xe1\x05\x13\xa9\xe3\x0e\xeb\x7f^\xfb\xf1\x1e\x01~!\xb3kW\xe0\xb1\x9d\xefQ\x8a\xa6\x84\xe9:\xd4\xd1(\xac`\x05\xd8\xfbF\xd0\x17*\\\x9c5\xf8\xa9o\x13\x8e\x1e\xe2c\x91\x8d\xbcx\xe0*\x84 \xad<\xbc0\x9a\xbe\x12\xa7\x06KR:8\xca\xef\x01\x8d%\x88\xadiy\x93\x8aM;\xe2\x8b%\x05\xb4\x9aiV2K\x9bM\xefAj\xfa\x1fU\x10\x85\x0e\xcc\xbd\xbfj\xfc\xb68\x84>\xab\xa3\xfb\x08\x08\xc2\x1e\x87\xd20zv\xe5\xb6\xb6\xf2T/UY\xac\xb8\x11'C\x97\xbe\xe5#\xf4C\xa6\xa8b\x10\x8b\xf7\x04h\x97k\xfek\xae\xab\xe7\n\xac\xd3~Hf\xe2\xd3\xbb\x1bP\x7f\xdf\xfd\xc65y\x7f\x1e4\x18\x0b)\x8fg\x1f\xc2\xe9/Q\x96\xdcv\xea\x84\xc1\xb6\x17n\x98TW\x92\x9a\xe2kM\x1f\xe1z!\xe6\r\xb6;'9@\xb6\x82\x1a=\xa4\x1a\xf5o#t\x02A&\x98.\xee\xc8\xad\xa7\xc0\x12\x98+#\x1f"
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
  sport= 41238
  dport= https
  seq= 3396076370
  ack= 1206568129
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3047691967, 3979380706))]

###[ TCP ]### 
  sport= 41238
  dport= https
  seq= 3396076370
  ack= 1206568129
  dataofs= 8
  reserved= 0
  flags= PA
  window= 501
  chksum= 0x58da
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3047691968, 3979380706))]
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
      |   |  load= 'A\x04"\x96q\xee\x0fA\x0e\x1a\xdd\x82<\x0b`\xb84\xfe\xaf\xa2\x8fkzO\t\xfa8\xd8\x9e^k@\x8c\x93\xc8\x84\xbe\x8aY\xad<Y~\x00"!sz\xfa\x88\xdc\xa5\xc6<0\xb2\xee\x9f\xcc\x13I\x97w^\xbc\xda'
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
            |  load= "m\x19n\xf7\xe1\x19f3~\xf5\xeab\x10\xf8\xb3(\xfc\xf2\xc8\x03'\x8c\x12\xdd\x0ft\x97<v\xa8\x96G~\xbe\x14efl\xcd\xb9\x0c\xdf|\xbd\xf5\x99\xec\xec"
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= https
  dport= 41238
  seq= 1206568129
  ack= 3396076504
  dataofs= 8
  reserved= 0
  flags= A
  window= 506
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3979380708, 3047691968))]

###[ TCP ]### 
  sport= https
  dport= 41238
  seq= 1206568129
  ack= 3396076504
  dataofs= 8
  reserved= 0
  flags= PA
  window= 506
  chksum= 0x593e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3979380709, 3047691968))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.0
     len= 170
     iv= b''
     \msg\
      |###[ Raw ]### 
      |  load= '\x04\x00\x00\xa6\x00\x00\x01,\x00\xa0T^t$\x01-\xcewwS\xaduS\x14Fu\xce\xd8\x0bc\xd3\xf9\x84\x92\xcfG\xa6v\x93\xc4\x1b\xdcN\x16\xe5\x01\xc0\x96\xeeB|\x83\xe3\xaf\x17\xec24\xbc\xaews/\xaf\xe0X\xb8Y@q\x87Si\xec>:\xb3\xd6\xcc\xfe\xa1\xbaB\x87[\xfa\xa5\x81\x8f\xe5\xb4\xd6\xc5\xfa\'~[I\xff\xba\x93\x12\x93\x141\x01\xebUev8\x99\x11P\xd2\xa1E\x7f\xdaa\xd8P\xe0\xa3R"\x10U[\xb5\xa5\xb9\xbex\xde\xf3s\x81bF:$\x08\xb1\x15\x8b\xeb\x0f\x97\xd8\xa2\xa2\x91\xdc\xae~\xe7\x99JaVw\x9f\x91\'D\x93\xb2\xdeg'
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
            |  load= '\xefp\xa7\xaa\xea4D\xb7\x9d\xae\xa8\xdeUD\x06\x9a7\xcb/\xfc0\xcd\x14\x1f5\xb6\x93\xbb\xa6Ir AC\xebm\xbb\x10\x19#sMKZV\xca\xe9\xa5'
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= 41238
  dport= https
  seq= 3396076504
  ack= 1206568363
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3047691969, 3979380709))]

###[ TCP ]### 
  sport= 41238
  dport= https
  seq= 3396076504
  ack= 1206568363
  dataofs= 8
  reserved= 0
  flags= FA
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3047692823, 3979380709))]

###[ TCP ]### 
  sport= https
  dport= 41238
  seq= 1206568363
  ack= 3396076505
  dataofs= 8
  reserved= 0
  flags= FA
  window= 506
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3979381563, 3047692823))]

###[ TCP ]### 
  sport= 41238
  dport= https
  seq= 3396076505
  ack= 1206568364
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3047692823, 3979381563))]

<Sniffed: TCP:14 UDP:0 ICMP:0 Other:0>

# server force tls ssl 3 with openssl

# catwoman : openssl s_server -ssl3 -key /...key -cert /...crt -accept 443 -www
# batman : curl https://catwoman
# joker : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())

###[ TCP ]### 
  sport= 48904
  dport= https
  seq= 519708045
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (1396481523, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 48904
  seq= 2048631674
  ack= 519708046
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (547280276, 1396481523)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 48904
  dport= https
  seq= 519708046
  ack= 2048631675
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1396481524, 547280276))]

###[ TCP ]### 
  sport= 48904
  dport= https
  seq= 519708046
  ack= 2048631675
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x1383
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1396481524, 547280276))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.0
     len= 512
     iv= b''
     \msg\
      |###[ TLS Handshake - Client Hello ]### 
      |  msgtype= client_hello
      |  msglen= 508
      |  version= TLS 1.2
      |  gmt_unix_time= Thu, 03 Dec 2009 08:11:53 +0000 (1259827913)
      |  random_bytes= 53b9b5ea4db9403ee4dd724851e9b955af5e1e6380a6e1407c51ca95
      |  sidlen= 0
      |  sid= ''
      |  cipherslen= 118
      |  ciphers= [TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_DHE_DSS_WITH_AES_256_GCM_SHA384, TLS_DHE_RSA_WITH_AES_256_GCM_SHA384, TLS_DHE_RSA_WITH_AES_256_CBC_SHA256, TLS_DHE_DSS_WITH_AES_256_CBC_SHA256, TLS_DHE_RSA_WITH_AES_256_CBC_SHA, TLS_DHE_DSS_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384, TLS_ECDH_RSA_WITH_AES_256_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_CAMELLIA_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_GCM_SHA256, TLS_DHE_RSA_WITH_AES_128_GCM_SHA256, TLS_DHE_RSA_WITH_AES_128_CBC_SHA256, TLS_DHE_DSS_WITH_AES_128_CBC_SHA256, TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_SEED_CBC_SHA, TLS_DHE_DSS_WITH_SEED_CBC_SHA, TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDH_RSA_WITH_AES_128_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_SEED_CBC_SHA, TLS_RSA_WITH_CAMELLIA_128_CBC_SHA, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_EMPTY_RENEGOTIATION_INFO_SCSV]
      |  complen= 1
      |  comp= null
      |  extlen= 349
      |  \ext\
      |   |###[ TLS Extension - Server Name ]### 
      |   |  type= server_name
      |   |  len= 13
      |   |  servernameslen= 11
      |   |  servernames= [b'catwoman']
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
      |   |###[ TLS Extension - Signature Algorithms ]### 
      |   |  type= signature_algorithms
      |   |  len= 32
      |   |  sig_algs_len= 30
      |   |  sig_algs= [sha512+rsa, sha512+dsa, sha512+ecdsa, sha384+rsa, sha384+dsa, sha384+ecdsa, sha256+rsa, sha256+dsa, sha256+ecdsa, sha224+rsa, sha224+dsa, sha224+ecdsa, sha1+rsa, sha1+dsa, sha1+ecdsa]
      |   |###[ TLS Extension - Heartbeat ]### 
      |   |  type= heartbeat
      |   |  len= 1
      |   |  heartbeat_mode= peer_allowed_to_send
      |   |###[ TLS Extension - Padding ]### 
      |   |  type= padding
      |   |  len= 223
      |   |  padding= '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
     mac= b''
     pad= b''
     padlen= None

###[ TCP ]### 
  sport= https
  dport= 48904
  seq= 2048631675
  ack= 519708563
  dataofs= 8
  reserved= 0
  flags= A
  window= 506
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (547280277, 1396481524))]

  pubnum = import_point(curve, self.point)
###[ TCP ]### 
  sport= https
  dport= 48904
  seq= 2048631675
  ack= 519708563
  dataofs= 8
  reserved= 0
  flags= PA
  window= 506
  chksum= 0x1654
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (547280279, 1396481524))]
###[ TLS ]### 
     type= handshake
     version= SSLv3
     len= 94
     iv= b''
     \msg\
      |###[ TLS Handshake - Server Hello ]### 
      |  msgtype= server_hello
      |  msglen= 90
      |  version= SSLv3
      |  gmt_unix_time= Tue, 22 Apr 2036 05:20:15 +0000 (2092454415)
      |  random_bytes= 6c42a388ba5fdf4b5f072a196fbf9d0eae588ee8dedbbf91fbd622dd
      |  sidlen= 32
      |  sid= '\xe9B|\x17\x93\xb4\xb3r\xc7<\xfbA\xf7\x17\xc2\xa2\x86\xe5\xa5\xba{B\xb7\x9e\x0b\x9a\xe5X\xbe\xf3m\xd8'
      |  cipher= TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
      |  comp= null
      |  extlen= 18
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
      |   |###[ TLS Extension - Heartbeat ]### 
      |   |  type= heartbeat
      |   |  len= 1
      |   |  heartbeat_mode= peer_allowed_to_send
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
            |   |  point= '\x04\xc9vAT\x1f`R\x90\xf0Z\x85\xa2\xa2\xdc\x01\x94\x05b[TAX\xa3\xf4a\x14o\xc1\xbc+\n\xd1:\x05\x06\xa2\x044m\xb4\xdeX\xe2GP2\x9f\xe3\xa4\x8a\xf2s\x9d\xd7"$\x93yA\xce\xa7\xa6\xc9\xc2'
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= "^\xda\x0c\xe1k\x99\x86(\x01\xaaF\x98\xb2\x03\xc7cX^z\x90\x86U|;\xb7\x18k\xa7\x7f\xde\x1c&\xd9n\xeb\xb8\x9aC\x87\xa9X\xc9PO\xa1\x8c\xfd\x1d\x9dz\x993\xd0lr\x02\xb1_\xa3\x8d\xf7C\x8e\x90\xc7\x05k\xe8Z_}~\xb0\xcf\x15l\x87*6\x1e\xe3\x16\xa1I\xb9_\x08\x11\xc2d\xc8\x0bN\xf5\xfb>P\xbea\xc9\xae\xbe\xe9`\xdeI\x9b\x8b\xa4\xcf\xad\xb6\xaa\xc8\x93\xbd\x8c\x93\xc4\x9efOJkCV\xf3\xa10X>\xfb.j\xd3\xc9;v\xe5\xb6\xe2\xaf\xaf\xf2\x91\xe81\x9c\xe5\x1aN\xb9\xb7\x98\xb9|\xfah\x97?wpm\xf4vw\xc87\xcc\x92\x8fn+\xd65\x82\x8c\xac\x86&\xf5RR\x14\x91\x061\xb7\xee^\xa2aP\x9f\x80\xa5\xf1}[~\xe3g5'p\xb0\xbez\xb1A\xce>e\xba\xe6m\xf0\xa1\x9a\x9e\xd4\x1f\xa4E\xfb\xe7\xd7\xfdEl\x0e\xba!\xdek\xb0\x12\xc0\xc1\xce\x9a\xd0D]\xdc\x82\x13R\x88\xee\x89\x99\xe6\nb\xf0"
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
  sport= 48904
  dport= https
  seq= 519708563
  ack= 2048632913
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1396481526, 547280279))]

###[ TCP ]### 
  sport= 48904
  dport= https
  seq= 519708563
  ack= 2048632913
  dataofs= 8
  reserved= 0
  flags= RA
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1396481526, 547280279))]

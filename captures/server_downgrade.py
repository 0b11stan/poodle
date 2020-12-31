##
# Server refuses tls 1.2, tls 1.1 and tls 1.0 with openssl
#   morpheus : openssl s_server -key /...key -cert /...crt -accept 443 -www \
#                -no_tls1_2 -no_tls1_1 -no_tls1
#   trinity : openssl s_client -connect morpheus:443
#   smith : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())
##

###[ TCP ]### 
  sport= 42884
  dport= https
  seq= 2363499937
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x5859
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (2277923831, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 42884
  seq= 4099286010
  ack= 2363499938
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x5859
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3126597767, 2277923831)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 42884
  dport= https
  seq= 2363499938
  ack= 4099286011
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277923831, 3126597767))]

###[ TCP ]### 
  sport= 42884
  dport= https
  seq= 2363499938
  ack= 4099286011
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x5972
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277923831, 3126597767))]
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
      |  gmt_unix_time= Tue, 22 Jan 2030 13:33:11 +0000 (1895319191)
      |  random_bytes= 387bc7505aa9c12d3fb4cde5350aba0ada9950c9ba6e5c232fbe6322
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
  dport= 42884
  seq= 4099286011
  ack= 2363500227
  dataofs= 8
  reserved= 0
  flags= A
  window= 507
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126597767, 2277923831))]

###[ TCP ]### 
  sport= https
  dport= 42884
  seq= 4099286011
  ack= 2363500227
  dataofs= 8
  reserved= 0
  flags= PA
  window= 507
  chksum= 0x5d27
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126597771, 2277923831))]
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
      |  gmt_unix_time= Tue, 20 Apr 2038 03:32:19 +0000 (2155347139)
      |  random_bytes= ad473eda733edb7c0c90b4a38fea6451bf45dd2d9044ef6e8fc1faeb
      |  sidlen= 32
      |  sid= 'XI\x8d\x81@O@\xeb\xd4\xd5\x9c\xc2\x9e#\xc1\x9b\xd0\x84\xe0\xa0\x92\xa5\xa8\x94\xc9zFhG\x19\x96z'
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
            |   |  point= "\x04+\x11\xfe^\xe84\xbc\n\xe6\xb9\x1b\xa6\x08\xfc\xa0\x83\x0bPz\xc2\x93\xe2\x03\xdd2\xf4\x16z\xd9\xc4\xb8\xc1\xf3|\x8b\x9a'\xf9\x93A\xc8\xf5\x12\x00\x04\xe6\x1d\xc3\xc8w-\xda$\x0e(\x13\x81\xe1\xe8\x12\xee\xb1\x0c\x15"
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= '}\x048\x82\xa6!Y\x1f\xd0\xec\x84\xaa\xd7\xe2\'\xd0\xe6\xd3\xf3H\xd2BP\x10w\x87\x16F\xa5\x04\xfd"\x86\xb9\xce[\xa9\xee\x84\x15~\xe7\x10\xd9\xad\rTd\x0b\x1b\xf7\x1e(\xcd\x8f\xe9bg\xa2\x1c\t\x1coF\x0e\x94\xf9\xfe\xf9\xe5\xcb\xf0NH\xa2=\x9d3;\x94\xf4\xb4\x0c\x90\xb8\\\xf9U\xd6\xee\xa6N\xc2r*dXrH\xe6Y\x9d:0\xeaG6g)\xabZ\xc5\xf7\x84\xb8=\xe0".Y\x80\xce\xee\\5c7o\x91\xf0m?\xf9\xb4\n,"\x19f\xf8\xc7\xe8g \xd1\xda\xc7\r\xa4\xbb\xd2\x18\x84"\xd8io\x97\xa3\x13\xcb\x1f\x02\x86M!\xab\x87g\xcd~l\xd1\x8a\xf83`fN\xf0\xc4\x00\xa7uI\xf2\xe1Y\xaa\x97\x1a?\xed#\xb9Oe\xe6Y\xbcZ\xbaOt\x82k\xa6\x19\xd4\xbe\x8c\x96KV\xd7\xfd\x8f\xa5\x1fO\xc2\xf2:\x08\x08`\xe9q&\x0f(\x9a\xce\xfb\xc6\x0fm)\t\xfe\xb3\xbb\x7f\x19W\x0b3\xf6\x7f<\x80\xefO\x90\xdc\xd4'
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
  sport= 42884
  dport= https
  seq= 2363500227
  ack= 4099287249
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277923835, 3126597771))]

###[ TCP ]### 
  sport= 42884
  dport= https
  seq= 2363500227
  ack= 4099287249
  dataofs= 8
  reserved= 0
  flags= PA
  window= 501
  chksum= 0x58e7
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277923835, 3126597771))]
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
      |   |  load= 'A\x04\xaa\x7fxL\x92RF\x0b\x8cA\xb7Ad\xc1\n\xe3z\xf1\xee\xbf\x8c\x8a\x915G\xc8\xf23R7\xc9\x07\x95\xb9\x8a~\xf17\xe3\xe0\x87\x87\xdb|\xfc\xcf@\xa4\x14\xe9\xd1\x87c\xb7];\x11\x19\x18\x8e\xdc*\xf6\xb7'
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
            |  load= '\x80\x0e\x07\x86\xaa\xd5\x87,\x9e?\x809#\xe3\xf6\xcbf\x92\xf8.\xd1\xee"\xdeV)\x0f\xf5-\xe6{[\xe7\xff\xef\x9b\xd9ZK\x19\xb6\xdc\r\',1\x88\x96yl\xf2\xbbpI 4\xd9^\xf2!\xbb\xdd\xc17'
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= https
  dport= 42884
  seq= 4099287249
  ack= 2363500377
  dataofs= 8
  reserved= 0
  flags= A
  window= 506
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126597772, 2277923835))]

###[ TCP ]### 
  sport= https
  dport= 42884
  seq= 4099287249
  ack= 2363500377
  dataofs= 8
  reserved= 0
  flags= PA
  window= 506
  chksum= 0x589c
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126597772, 2277923835))]
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
         |  load= "+\xe1\xa1\x17\xfe\x8a\x99\xb6\xb7\xa4\x96\xe2\x92\xad\xa1\xe2\x1c\x03{\xef\xcbo\x0c8QQ\xe9\xcf\xcb\x91&\xb6H4\xe3Y\x8a`\x08n\x8361\xba\x1b\xf4\xcbq2*\xa4\xd2\x98\x06\x8bb\xd0\x96*N^~\xfd'"
        mac= b''
        pad= b''
        padlen= None

###[ TCP ]### 
  sport= 42884
  dport= https
  seq= 2363500377
  ack= 4099287324
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277923836, 3126597772))]

###[ TCP ]### 
  sport= 42884
  dport= https
  seq= 2363500377
  ack= 4099287324
  dataofs= 8
  reserved= 0
  flags= FA
  window= 501
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277925293, 3126597772))]

###[ TCP ]### 
  sport= https
  dport= 42884
  seq= 4099287324
  ack= 2363500378
  dataofs= 8
  reserved= 0
  flags= FA
  window= 506
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3126599229, 2277925293))]

###[ TCP ]### 
  sport= 42884
  dport= https
  seq= 2363500378
  ack= 4099287325
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5851
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (2277925293, 3126599229))]

<Sniffed: TCP:14 UDP:0 ICMP:0 Other:0>

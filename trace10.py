# server refuse tls 1.2, tls 1.1 and tls 1.0 and client force sslv3 with openssl

# catwoman : openssl s_server -key /...key -cert /...crt -accept 443 -www \
#              -no_tls1_2 -no_tls1_1 -no_tls1
# batman : openssl s_client -connect catwoman:443
# joker : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())

###[ TCP ]### 
  sport= 56008
  dport= https
  seq= 3556361340
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x5861
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (117668062, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 56008
  seq= 2440459204
  ack= 3556361341
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x5861
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (1372246718, 117668062)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 56008
  dport= https
  seq= 3556361341
  ack= 2440459205
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x5859
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (117668063, 1372246718))]

###[ TCP ]### 
  sport= 56008
  dport= https
  seq= 3556361341
  ack= 2440459205
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x597a
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (117668063, 1372246718))]
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
      |  gmt_unix_time= Thu, 19 Jul 2063 02:37:04 +0000 (2952038224)
      |  random_bytes= 785ed24c14b42417d26922e62b689853be082116096671afe7a5c7cd
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
  dport= 56008
  seq= 2440459205
  ack= 3556361630
  dataofs= 8
  reserved= 0
  flags= A
  window= 507
  chksum= 0x5859
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1372246718, 117668063))]

/usr/lib/python3/dist-packages/scapy/layers/tls/keyexchange.py:588: CryptographyDeprecationWarning: Support for unsafe construction of public numbers from encoded data will be removed in a future version. Please use EllipticCurvePublicKey.from_encoded_point
  pubnum = import_point(curve, self.point)
###[ TCP ]### 
  sport= https
  dport= 56008
  seq= 2440459205
  ack= 3556361630
  dataofs= 8
  reserved= 0
  flags= PA
  window= 507
  chksum= 0x5d2f
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1372246719, 117668063))]
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
      |  gmt_unix_time= Mon, 16 Oct 2056 00:25:03 +0000 (2738881503)
      |  random_bytes= e56f22eef5af9d01eb1261ddeb3da4a480ce760046fcd6516da0781f
      |  sidlen= 32
      |  sid= '\xa6\xb1\x80\\\xfe\xc0{\xfb\xf6\xeb3\xe4{\x15\xdf\x199\x99\xbf}f\x89Y\xa5#|.\xbajv\xee='
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
            |   |  point= "\x049\xdc\r\xc1\x87\xa4eYN\xd3\xcc\x0b\r\xfb=\xad`G\xff\xdc\xe5\x06\x81\xc7N\x08\nN\x1a\xe8\x1b\xa8\x12\x97fl{VN\xad\x18?\xc5\xac\x9b\xb0'[%\xe1\xa6~\x94w-\xfe\x94\xdd\xdci\xe9\xdf\x83\xf0"
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= '\x11\x84 ?\xdb\x94BL\x0bGY))\x91\xb7\xea\x05>F1\x80\x03b\xd7\xb2\x92)\xd86\xe8[`\xe7\x08+\x18P\xa8{h\x1d\x11\x88Q\xc8\xca=K#c\x94\xbc@\\\x98\x0b\x16Y:\x8dluP\x97\xe1JH\x88\xbdF\xea\x0e\xf7\xdc:f\x90\xa1\xb2\xe2\xe0\xc0\x87\xd2\x05&\xc0c\xf2\x15K\x17zj\x92\x04\xe7aty~\n\x19\xbd\x1e\xf5\x0b\xb8)\xcf\xefs\x06\x80\x01\x94\x07\xbe\xa6D\xc0s\x1e`8\xd9\xba<\xa5\xeb\xe6&\x12%}\xe4\xd2\x1c\xf96\x96\x87\x8f\xaeP\xb8]%\x10\xc5v\x0b\xc8\x99\xb0n@=y\xcc\xc9/\xcfy`y\xf0\x89\x86\xf5,;\xdb\x06\x0c\xf9\x9d\n\x17\xbc\xafT<\xc5S\xc9\x8e\xd8\xaaP\xda\x11z\x07\xb4\xffB\x81}P>T\xc9\x99\x7fp\xa6`\xc4\xf7"\xe6\xfe\rs\x89\xfcB\xba\xa3i\x9b\x9b\x93\xcdD\xe1\x82\x17E\xee\xb3\xae\x8bl:P\ns\x9d\xaaz\xe0\x82\xf4\t\r\xe8\x19E\'k\x98\xfd\xfa\xcf'
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
  sport= 56008
  dport= https
  seq= 3556361630
  ack= 2440460443
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5859
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (117668064, 1372246719))]

###[ TCP ]### 
  sport= 56008
  dport= https
  seq= 3556361630
  ack= 2440460443
  dataofs= 8
  reserved= 0
  flags= PA
  window= 501
  chksum= 0x58ef
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (117668065, 1372246719))]
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
      |   |  load= 'A\x04\x7f\xb1\r\x8b\xfb/\xa3\x1d9!\xc9\xb3\xb6F\x99,\xedX\xe4\xda\xdbn\x06\x00F\x160\xe0L!\xd1\x9fr@\xf7\xcc:b\x08\xa7\xe8\xea\x91\xa0N\xf1\x87\xfb;|\xe7}E(\x8b\x18\xb2\x1dY\x0c\x8c\x87\x033'
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
            |  load= 'kD\x8b#\xa2-\xa9v\xf8\t\xf1<\x1c\xbcW\xf8\xb4\xa5\xea\xf8\x14\xf2\x8e\x8cCZ\xbb\x9f\xc7\x99\x0bB\x86\xee\xafJ1Mn\x14\xf2k\xf8\xb5\xc7\xcd\x9a\x14\xf9mI\xb5:t\x1a\xea\xb3xU\xc2sK}\xe3'
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= https
  dport= 56008
  seq= 2440460443
  ack= 3556361780
  dataofs= 8
  reserved= 0
  flags= A
  window= 506
  chksum= 0x5859
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1372246720, 117668065))]

###[ TCP ]### 
  sport= https
  dport= 56008
  seq= 2440460443
  ack= 3556361780
  dataofs= 8
  reserved= 0
  flags= PA
  window= 506
  chksum= 0x58a4
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1372246720, 117668065))]
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
         |  load= '%\xfc)I\xc1\xee\xcc\xe0\x90\xcdj\xb3\xc0\x99I;\xa5q\x8d\x03\xed=\xce\xa7\xf9!\xf6\x1cye\x8cDQ)\xdd\n\xe6\xc0\xdf\xad\xc1q\x0f\x7f\x83\\\xf4\x0e\x06\xb1\xe0\xc4K\\\xd9U\x00G\xfeK\xdc\x92\nq'
        mac= b''
        pad= b''
        padlen= None

###[ TCP ]### 
  sport= 56008
  dport= https
  seq= 3556361780
  ack= 2440460518
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5859
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (117668065, 1372246720))]

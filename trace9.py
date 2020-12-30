# server refuse tls 1.2, tls 1.1 and tls 1.0 and client force sslv3 with openssl

# morpheus : openssl s_server -key /...key -cert /...crt -accept 443 -www \
#              -no_tls1_2 -no_tls1_1 -no_tls1
# trinity : openssl s_client -connect morpheus:443 -ssl3
# smith : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())

###[ TCP ]### 
  sport= 48212
  dport= https
  seq= 3862036455
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x585c
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3051005578, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 48212
  seq= 80861918
  ack= 3862036456
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x585c
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3982694318, 3051005578)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 48212
  dport= https
  seq= 3862036456
  ack= 80861919
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051005578, 3982694318))]

###[ TCP ]### 
  sport= 48212
  dport= https
  seq= 3862036456
  ack= 80861919
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x5975
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051005578, 3982694318))]
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
      |  gmt_unix_time= Mon, 02 Nov 1998 21:34:13 +0000 (910042453)
      |  random_bytes= cf041a1bea371c1ee979a064f53f01c6db2ea5a82643fba18d8254b0
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
  dport= 48212
  seq= 80861919
  ack= 3862036745
  dataofs= 8
  reserved= 0
  flags= A
  window= 507
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3982694318, 3051005578))]

  pubnum = import_point(curve, self.point)
###[ TCP ]### 
  sport= https
  dport= 48212
  seq= 80861919
  ack= 3862036745
  dataofs= 8
  reserved= 0
  flags= PA
  window= 507
  chksum= 0x5d2a
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3982694321, 3051005578))]
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
      |  gmt_unix_time= Tue, 30 Sep 2059 18:05:27 +0000 (2832170727)
      |  random_bytes= e531d6a6b1c3775783430e964aaeb042c41ae417a3eed5c451e07621
      |  sidlen= 32
      |  sid= '\xd1\xdbD\x8e\xc3\x87\xef\xd7\x02p\x1aA5X\xeb\x04\xbeN\x7f\xfe\x14\x9a\x8cl\x0b$\xd3@\x93\x041X'
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
         |  certs= [(779, [X.509 Cert. Subject:/CN=morpheus, Issuer:/CN=morpheus])]
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
            |   |  point= '\x04a\xa2\x01\x92;3\xdb\xfb\x14\xdc\xec\xc8:\xe0\xf6\xbcZc\x10\x92AC\x94\xadn</s>\xd6\xbagA\x9b\x82\xab\xf5\xd7\xcad\xaf\xe7\x94\x14\t\xda\x8c\xe4\xa0\x10\xf2\xbb\x1f\xf6\xd7\xb3\xda\x1a\xc2-\xb9t\x03@'
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= "\x80\xc0q\xed\xea\xf4a/\x07\xfa*\x9f'3_^6\xb0+,\xd8\x18\x9aii2\xc2z\x9aP\xc3u8\x1dOq\x0b\x11\xda\x03\xc9N\x04\x07zl\x1c\x0c\x99\x9e\x01\x99z\x94\xc6'\xff\x00d\xdb\xa5s\xdd\xf7\xe9-\xb3So58\xc1U\\\xbb\x844\x81\xe4Y3\x03b\nh\x8e\xd0[\xc03n\xea'cM\x1aNnt\xe2\xd7\xca\xccS \x04z\xcd\x8a\xe8\x96\x05\x07\x8cv\xc2!4\xb2\xf0\xb5\xef\x9b%\xd9\xe3\xfcd \xc6\x97\xebJ\x90\xc5\xc2\xc5J\x0e\xa1\xd0R\x11\xb5Q\x11b X\x16\x9c\x9a\x9c\x8c\xcd\xd4E\x14I\xdb\xf8\x13Fv\xd6\xb5bDB/\xad\x89\xf4\x0b\xcb\x16\x15<]M\rM\x08\xdd&\x9aC\x88\x9c\x97\x92\x18\xec\n\x02\xf9\x0e\x84MS\xd7\x971\x06\xf2\xed\x08;8\xbbKp\x16\x987F\x04\x0bk\xd7(\xaf\xa9\xd6\xb6|\x1eW\xc2\xf0L\xa2\x1b\x0c}^@m\xb7\x81t\xc6!\xca\xb8A\xe9j\x16\x97JL\xd3\xcc\xf4#"
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
  sport= 48212
  dport= https
  seq= 3862036745
  ack= 80863157
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051005581, 3982694321))]

###[ TCP ]### 
  sport= 48212
  dport= https
  seq= 3862036745
  ack= 80863157
  dataofs= 8
  reserved= 0
  flags= RA
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051005581, 3982694321))]

###[ TCP ]### 
  sport= 48234
  dport= https
  seq= 753012895
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x585c
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3051014652, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 48234
  seq= 493352684
  ack= 753012896
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x585c
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3982703392, 3051014652)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 48234
  dport= https
  seq= 753012896
  ack= 493352685
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051014652, 3982703392))]

###[ TCP ]### 
  sport= 48234
  dport= https
  seq= 753012896
  ack= 493352685
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x58ce
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051014652, 3982703392))]
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
      |  gmt_unix_time= Sat, 22 May 2100 07:41:16 +0000 (4114654876)
      |  random_bytes= e18454997d47f94b0ef6fbc138b8cd82c74fdcbc157745c4f408739d
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
  dport= 48234
  seq= 493352685
  ack= 753013018
  dataofs= 8
  reserved= 0
  flags= A
  window= 509
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3982703392, 3051014652))]

###[ TCP ]### 
  sport= https
  dport= 48234
  seq= 493352685
  ack= 753013018
  dataofs= 8
  reserved= 0
  flags= PA
  window= 509
  chksum= 0x5d1d
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3982703394, 3051014652))]
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
      |  gmt_unix_time= Sun, 02 Jan 2095 09:33:09 +0000 (3944799189)
      |  random_bytes= e5a4daebfc52bd8751437cf49e313b052a431e95e7e68e1cfa830725
      |  sidlen= 32
      |  sid= '\xdeF\xf4>dB\xc91w\xf6bu\xd6}\xbd\xeen\x91\x02\xab\xa6\xd6?\x12\x94\xce\xb5A\xf2f\x99Q'
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
         |  certs= [(779, [X.509 Cert. Subject:/CN=morpheus, Issuer:/CN=morpheus])]
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
            |   |  point= '\x04a\xa2\x01\x92;3\xdb\xfb\x14\xdc\xec\xc8:\xe0\xf6\xbcZc\x10\x92AC\x94\xadn</s>\xd6\xbagA\x9b\x82\xab\xf5\xd7\xcad\xaf\xe7\x94\x14\t\xda\x8c\xe4\xa0\x10\xf2\xbb\x1f\xf6\xd7\xb3\xda\x1a\xc2-\xb9t\x03@'
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= '\x16\xb1A\x99\xbapk\xaa\x0e=\x97;\x1ex\x0bM7\xce\xd8\xdcI\xddd\x9b<\xe8\n\xef\x84\x01&\xd7\x93`\x89\xbb\x1aa\x1f+LS\xd3\xeb\xe7O\xefI\xc0\n\xcf\x8a\x84\x05\x9d\xb2{`\xd9\xb14%\xe0\x86%\xe0]\x86\xcdC\xed!\xe7\xd1\x93BH\xde\x80\xc5\xfaD\xfc\x93!d\xe1v=j\x02n&\x96-\x06\xd2\xbf\x91\xe4\xc9\xc9!\xe6urKT\x1eR\xe5<C\x8b\\o\xafx\xa9Y,L\xc5\xec\xa3S5\xf9\xf6\xcf\x80J\x04\xc2J\x99\\\x046\xc0\xf0x\x83\xbd\x9c\x93\xc9\xcad\xf5c`\xe9|.8+*W\xe4\x186\x8e\xfe\x93B\xb7\xe9\xff\xab\x83\xdc\xb4\xe4\xfe\x88w\x95\xbe\xeb8\xc8}\x1aQ\x8d\x8e3\xe18\xa7\x18gR6\xb3M#\xa9#]_\x1b\xd6,\x88\x06\xcbDI_\xe1\xa8\xa5\xd5hi\xe9S#%8\xc5\x04\xe6@\x87K(e\x15\x8b\xa1\x88D\x93LIwr\x1c\n9\xe0I\xf4\xdc\xb6+\xbaO\xe3\xefm\xcd\xff'
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
  sport= 48234
  dport= https
  seq= 753013018
  ack= 493353910
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051014654, 3982703394))]

###[ TCP ]### 
  sport= 48234
  dport= https
  seq= 753013018
  ack= 493353910
  dataofs= 8
  reserved= 0
  flags= PA
  window= 501
  chksum= 0x58ea
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051014655, 3982703394))]
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
      |   |  load= 'A\x04\x89\xef\xaeb\n\x17GF\xc6\xab\x12\xdaV\x01\x01\x00\xb9\x94\t\xbc\xca]\xc4\xaa\x8e\xb0\xa5\xa8\x02@\xa0\x91\x8e\xcfJ\xc5u\x16s\x8f\xa4\x85\x0e\x88\xda\xcbJ\xd5\xc5\xd8\xb7\x8d\xe9\x8d\xb4\x80n\xcba\xb3-\xd1\xd4m'
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
            |  load= "\x86'\x9e`\x0b8]\xd9S4\xcfS\x01F\xaf\xa7\xd0\x90\x82\xbd=\x08\x95R]n\xe3hJE\xef\xca\x9e\xd7\xff\x8a[\xa24\xc9\x84?\x8e\xbf\xa5\x95c\xd0\xef\x90d~E0\xf6\xd7\xed\xd4L\x10#\x9b\xb5\x1c"
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= https
  dport= 48234
  seq= 493353910
  ack= 753013168
  dataofs= 8
  reserved= 0
  flags= A
  window= 508
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3982703396, 3051014655))]

###[ TCP ]### 
  sport= https
  dport= 48234
  seq= 493353910
  ack= 753013168
  dataofs= 8
  reserved= 0
  flags= PA
  window= 508
  chksum= 0x589f
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3982703396, 3051014655))]
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
         |  load= 'v\x18*\t\xe1=)\x8b\x99c\xcd&\x82\x1a\xc7=G-\x16O\xcdp\xae\x06\xb7\x00\x1a\xfbM\xbfi\xb4\x9f\xd0\xd6\x18\xf3t\xa0\x97\x97\x95\x9dd>\x03t\xad\xe9\x8fk\xbcl\x1a\x1e\xba)q-DL\xb0\x01b'
        mac= b''
        pad= b''
        padlen= None

###[ TCP ]### 
  sport= 48234
  dport= https
  seq= 753013168
  ack= 493353985
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051014656, 3982703396))]

###[ TCP ]### 
  sport= 48234
  dport= https
  seq= 753013168
  ack= 493353985
  dataofs= 8
  reserved= 0
  flags= FA
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051099935, 3982703396))]

###[ TCP ]### 
  sport= https
  dport= 48234
  seq= 493353985
  ack= 753013169
  dataofs= 8
  reserved= 0
  flags= FA
  window= 508
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3982788675, 3051099935))]

###[ TCP ]### 
  sport= 48234
  dport= https
  seq= 753013169
  ack= 493353986
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x5854
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (3051099936, 3982788675))]

<Sniffed: TCP:22 UDP:0 ICMP:0 Other:0>

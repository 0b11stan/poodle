# ssl3 is forced on both sides with openssl

# morpheus : openssl s_server -ssl3 -key /...key -cert /...crt -accept 443 -www
# trinity : openssl s_client -ssl3 -connect morpheus:443
# smith : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())

###[ TCP ]### 
  sport= 46858
  dport= https
  seq= 518720794
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (1395472264, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 46858
  seq= 2891728944
  ack= 518720795
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (546271018, 1395472264)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 46858
  dport= https
  seq= 518720795
  ack= 2891728945
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1395472265, 546271018))]

###[ TCP ]### 
  sport= 46858
  dport= https
  seq= 518720795
  ack= 2891728945
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x11f8
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1395472265, 546271018))]
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
      |  gmt_unix_time= Tue, 12 Feb 1974 06:41:30 +0000 (129883290)
      |  random_bytes= 57a178d53ebc3dd63b955ef8c73efe6e363a61ed284d1be7878b6720
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
  dport= 46858
  seq= 2891728945
  ack= 518720917
  dataofs= 8
  reserved= 0
  flags= A
  window= 509
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (546271018, 1395472265))]

  pubnum = import_point(curve, self.point)
###[ TCP ]### 
  sport= https
  dport= 46858
  seq= 2891728945
  ack= 518720917
  dataofs= 8
  reserved= 0
  flags= PA
  window= 509
  chksum= 0x1647
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (546271019, 1395472265))]
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
      |  gmt_unix_time= Sun, 29 Jun 2014 14:15:22 +0000 (1404051322)
      |  random_bytes= 0b82b1d9bb2ac2d7917d39b6b7043d2b3db6a719d54b9f47b603e043
      |  sidlen= 32
      |  sid= '\x07\xca\xbe\xae3\\\x04\xe7\x9e\xba`\x05\xcb\x9f\xb2\xe7\x815J\x81\x99\x10\x19\xd1\x08$\xdb\n\xf5\xbe\x06\xaa'
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
            |   |  point= '\x04\xc9vAT\x1f`R\x90\xf0Z\x85\xa2\xa2\xdc\x01\x94\x05b[TAX\xa3\xf4a\x14o\xc1\xbc+\n\xd1:\x05\x06\xa2\x044m\xb4\xdeX\xe2GP2\x9f\xe3\xa4\x8a\xf2s\x9d\xd7"$\x93yA\xce\xa7\xa6\xc9\xc2'
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= 'tm\xadg:\xfa\xf1C\x12E\n\xfb\xb1\xf7\xb1\xf7P\x94\xe7^\xfc\xf1\x10\t/\x03\xa5\xabr\x93\xd5S\xdc\x84\xf9\x9dyo\xd5\x94\x0f\x86\xac\x98\x94+\xde\x03W\xadV\xf0D\x89\xa8\xf6\xbc\xcc|\xe9k[\x87\xc3\xf4S9\xc2Kf$\x93q\x04\xd2\xcf\x9a\xe2\xd8de\x15?\x04|\x8a\x16\xfb\xd6\xcb\x02\x10\xff%=\xc3\xf8YE6\xdd{\xdd\'\xbam\x88\xcf{-\x89\xf9\xbc\x82nH\xdexj\xaa\x82!\x87\xdc\xa7\xe9\xe2\xc8\xe6\xa7\x82\x0e\xa6\x95\xa0G\x1a(\xcf\xe8A\x10\xfa\xc7T\xba\xbd\xd9#\x1e\xaa3\xb1\n\x06\xcc\x0f"\xe0\x13\x0e\x95\xf5\xef\x0b\xbb+\x11\t\xa1;\xf6\xc7\xde\xf0\x96\xbd\xec\xa9\xcflM\xe4\x136E\x02\'\xa9\x18\x10I0[\xf1\xf7\x90\xb7\xdeq\xd9\xa0-Nu$\xe4\xfbPiz\xeb\x0f\xbax\xbc\xbb\xee\xfd\x84\xa59!v\xef\xbfGH%\xa5\x87\x19L8\xf8\x0bE\xa5_\xa9\xb8.\x9a\xff\xefQ\x98\xad\x16oNK\xae\xf7\xcdG'
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
  sport= 46858
  dport= https
  seq= 518720917
  ack= 2891730170
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1395472266, 546271019))]

###[ TCP ]### 
  sport= 46858
  dport= https
  seq= 518720917
  ack= 2891730170
  dataofs= 8
  reserved= 0
  flags= PA
  window= 501
  chksum= 0x1214
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1395472267, 546271019))]
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
      |   |  load= 'A\x04}\x90D\x89\xa8kp\xd1\ry\xdai[n\xc4C&9\xabn\xdb\xa7\x8f\xef\xf1[\x1f\x04.R\x0eh\\\xaaG\x9a\xd0M\xdd[\xeb\x8c\xfb\x16\xbf\x04\x83\xeb8\x17+\x99\xf5\r\xe3QH\x98\xa2\x82\x88F\x83\x91'
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
            |  load= '"\xe2\xd0\x05\xf6\xdd\t\xa5Qh/\x03\x01F\x9a\xc2N\x9aB\xff\x1d\x91\xbd\x16\x8a`}\xe4S\xca\x96\xfbw\x92\\.7\x13\xbew\xb2\'\xa1\xe1\xe7\xb5\xed\x9a\x073\t\x1c-\x9e\xc2\x85\xf0|\xfbgs^Z\x1e'
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= https
  dport= 46858
  seq= 2891730170
  ack= 518721067
  dataofs= 8
  reserved= 0
  flags= A
  window= 508
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (546271020, 1395472267))]

###[ TCP ]### 
  sport= https
  dport= 46858
  seq= 2891730170
  ack= 518721067
  dataofs= 8
  reserved= 0
  flags= PA
  window= 508
  chksum= 0x11c9
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (546271021, 1395472267))]
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
         |  load= 'zg%,l@\x9a\xdf\xb1I\r\x02\x8d\xc3\xad\xa9\x08Q\x12xQ\xba\xca\xe9N\xf5\x0b[:\x0f\r\xf8\xf8\x8d\'d"s\x04\xf2\x1b\x8f$S\xbc\xd9\xbev\xfc+\x05MG`\xb6\xd4\x88\xcf\xd4\x9a\x98\xbd\x1a\xed'
        mac= b''
        pad= b''
        padlen= None

###[ TCP ]### 
  sport= 46858
  dport= https
  seq= 518721067
  ack= 2891730245
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1395472268, 546271021))]

<Sniffed: TCP:11 UDP:0 ICMP:0 Other:0>
`

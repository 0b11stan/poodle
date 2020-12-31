# server refuse tls 1.2 with openssl

# morpheus : openssl s_server -key /...key -cert /...crt -accept 443 -www \
#              -no_tls1_2
# trinity : openssl s_client -connect morpheus:443
# smith : sniff(iface="eth1", filter="tcp", prn=lambda p: p["TCP"].show())

###[ TCP ]### 
  sport= 54926
  dport= https
  seq= 977244345
  ack= 0
  dataofs= 10
  reserved= 0
  flags= S
  window= 64240
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (1399375679, 0)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= https
  dport= 54926
  seq= 702155533
  ack= 977244346
  dataofs= 10
  reserved= 0
  flags= SA
  window= 65160
  chksum= 0x1186
  urgptr= 0
  options= [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (550174432, 1399375679)), ('NOP', None), ('WScale', 7)]

###[ TCP ]### 
  sport= 54926
  dport= https
  seq= 977244346
  ack= 702155534
  dataofs= 8
  reserved= 0
  flags= A
  window= 502
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1399375679, 550174432))]

###[ TCP ]### 
  sport= 54926
  dport= https
  seq= 977244346
  ack= 702155534
  dataofs= 8
  reserved= 0
  flags= PA
  window= 502
  chksum= 0x129f
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1399375679, 550174432))]
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
      |  gmt_unix_time= Tue, 27 Nov 2057 09:02:31 +0000 (2774077351)
      |  random_bytes= 42fe66aad98288cc475c1a5fb1c1ca91a9bcdc8cde7ccf475229d263
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
  dport= 54926
  seq= 702155534
  ack= 977244635
  dataofs= 8
  reserved= 0
  flags= A
  window= 507
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (550174432, 1399375679))]

  pubnum = import_point(curve, self.point)
###[ TCP ]### 
  sport= https
  dport= 54926
  seq= 702155534
  ack= 977244635
  dataofs= 8
  reserved= 0
  flags= PA
  window= 507
  chksum= 0x1638
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (550174434, 1399375679))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.1
     len= 66
     iv= b''
     \msg\
      |###[ TLS Handshake - Server Hello ]### 
      |  msgtype= server_hello
      |  msglen= 62
      |  version= TLS 1.1
      |  gmt_unix_time= Sun, 31 Aug 2042 03:29:06 +0000 (2293068546)
      |  random_bytes= b51b7f1464950b94aee65f35f7c74b0018ced9c160ca3c3711196f9f
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
        version= TLS 1.1
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
           version= TLS 1.1
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
            |   |  point= "\x04y\xfb\x07\xa6\x9d\xe1\xd6(G\xcc\xdb\xd8\xea\xaa\xd0\x98\xdb\x0c\x94\x1c\x8ag\xa0\x1c'\xbb_\x1a*\xc1\xf6q\x0c\x9f2\n\xde\xc9|\xb1\x18\x10 e\x08r\x97\xf6|\xc7\x1f\xfc\x96\xae/\x82\xcf\x89\xf1.!\x01\xd0\x0b"
            |  \sig\
            |   |###[ TLS Digital Signature ]### 
            |   |  sig_alg= None
            |   |  sig_len= 256
            |   |  sig_val= "\\\x8d=Y=a(\xff\x7f8\xbf\xd75\xad^j\xa7\xc2\xbe\x17h4h\x1d\x8a\xaf\x0fMw\xe9/\x14\x80\xdb\xe5o\xe2\x91M%7p\t\xde[\xde\x8e\x02\x9d\xa9o\x9a\x17QK/Z\x05b\x99\x0b2\t,*&}.I\xe0\xfc\xe597\x82J\xe2\xb6 \xf9\x88\xe7+\x08[;b\x85(]k\xaf\x07)\x89\xa6\xa4\x065\xeb+\xec2\xd9\xc5\xa91\x1e8\xd7\xc8\x08\xe1\xedP\xd8\x1d~?\xb2un\xa7\xbe{U\x0e\x86\x9c\xd4\xb1\xd8\xd0\xba\xd9\xf4\x94c\xa3\x01\x17\x959w\xdc\x1c\x19$M\xf5;\xa1\x88\x12\xf6A_\x84-\xdb%\x06\xc0?`8t\xaeh\xfb\xe0\xee\xbf\xaa\x83bE\xf0\x06\x9c\n5*\xe3+\xe1A\x1at\xff\xe6\n\xcd\x81+i\x13Q\xd26\xe6\x97\x9a\xbb\xafVcv\xcf\xebe'\xed\xef\xe5\xb9\xae\xde\xef\xfa\xb2_\xb7?\xfd\xd0]o\x98K\x1b\x0c\xa1.lD\xe5\x80Z\xa6\x16s\xdbG\xc5\xc8\xf4Z\xb9?N I\xd9\x98\xa4"
           mac= b''
           pad= b''
           padlen= None
###[ TLS ]### 
              type= handshake
              version= TLS 1.1
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
  sport= 54926
  dport= https
  seq= 977244635
  ack= 702156744
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1399375681, 550174434))]

###[ TCP ]### 
  sport= 54926
  dport= https
  seq= 977244635
  ack= 702156744
  dataofs= 8
  reserved= 0
  flags= PA
  window= 501
  chksum= 0x1214
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1399375682, 550174434))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.1
     len= 70
     iv= b''
     \msg\
      |###[ TLS Handshake - Client Key Exchange ]### 
      |  msgtype= client_key_exchange
      |  msglen= 66
      |  \exchkeys\
      |   |###[ Raw ]### 
      |   |  load= 'A\x04\x8d\x0b\x0e\x02|{\xf0N5Y\x0fwA\x102\xd3\x9bEd\xf7\x89\rK\xbe\x82\x8c\x12.\x1a\xc2\x7fMBQ\x16\x07t\x9a9\x96M\x1a~r\xd9\xa41\xf9\xd3\xdd\xea\xfds\xebi\xb3\xbb\x91\x96h\xbc\xb9w\x8d'
     mac= b''
     pad= b''
     padlen= None
###[ TLS ]### 
        type= change_cipher_spec
        version= TLS 1.1
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
           version= TLS 1.1
           len= 64
           iv= b''
           \msg\
            |###[ Raw ]### 
            |  load= '\x9a\x00\xb2\xe4\xbd=\xba\xaeo\x16gu\x85r\x9a\x10f\r\xcc[\x86\x07\x8f\xe7\xda\xe7\x0b\xad\xe9.l\xdf\x14t,F\xa5\xf0\xed\x1e\xd4P\xe82K\\B,d\xff4\x86\n\xbep0G,\xfd\xd8\x17c9)'
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= https
  dport= 54926
  seq= 702156744
  ack= 977244785
  dataofs= 8
  reserved= 0
  flags= A
  window= 506
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (550174435, 1399375682))]

###[ TCP ]### 
  sport= https
  dport= 54926
  seq= 702156744
  ack= 977244785
  dataofs= 8
  reserved= 0
  flags= PA
  window= 506
  chksum= 0x1278
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (550174435, 1399375682))]
###[ TLS ]### 
     type= handshake
     version= TLS 1.1
     len= 170
     iv= b''
     \msg\
      |###[ Raw ]### 
      |  load= "\x04\x00\x00\xa6\x00\x00\x01,\x00\xa0\xa9\x1e\xf2\xf3\xa4\x93\xb1\x9bM\x08V\x02\x116\x14\xac)\xd9\x80/\tT@\xd7G\x15\xa5\xa6\x8c\xa2A\xc3_\xa9\x04w\x89\x99\x8b1\x90\xcd\xf7/\x1e1?\xd5G\xf24A\xa3%6]\x86AmN\x00\xb2k\x04\xd10\xbf\xc5\xc9\x07\xb4\x0e\x13L\x02/e\xbf\xe0\xcdm\xce\x00\x84\x8dY'@xI\xf2\x04\xe6X\xb04:\xe6s\xb0I\x1c\x1a_\xff(s\xcb(\xfe\x06B\xdd\x88\xe0\xc5\xa7\xe2\xf0\x06aa(p\xccK\x91q\xf1\xe4$7aU\xc3\xd3>\xdb\xbet\xe0\x1e\x9ei\xa5\xd95IB\x84%\xb7\xcdci\x89\xce\x9f\x1e\xbe"
     mac= b''
     pad= b''
     padlen= None
###[ TLS ]### 
        type= change_cipher_spec
        version= TLS 1.1
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
           version= TLS 1.1
           len= 64
           iv= b''
           \msg\
            |###[ Raw ]### 
            |  load= 'I\xfd\x8cy\xb3a*<\xd7xT\x81N!\x85t\x120\xe4,K\xc1\x80\x1b$\xe3m\x81\x1d\xf5\xb7+\x12\x17\xad\x04\xd8\xa7[cG/r\xaf$n\x8a\x02\xe4}BAt\x80\xb2\x8aF\x1f2*\x19\x8b\x80\x14'
           mac= b''
           pad= b''
           padlen= None

###[ TCP ]### 
  sport= 54926
  dport= https
  seq= 977244785
  ack= 702156994
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1399375682, 550174435))]

###[ TCP ]### 
  sport= 54926
  dport= https
  seq= 977244785
  ack= 702156994
  dataofs= 8
  reserved= 0
  flags= FA
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1399377809, 550174435))]

###[ TCP ]### 
  sport= https
  dport= 54926
  seq= 702156994
  ack= 977244786
  dataofs= 8
  reserved= 0
  flags= FA
  window= 506
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (550176562, 1399377809))]

###[ TCP ]### 
  sport= 54926
  dport= https
  seq= 977244786
  ack= 702156995
  dataofs= 8
  reserved= 0
  flags= A
  window= 501
  chksum= 0x117e
  urgptr= 0
  options= [('NOP', None), ('NOP', None), ('Timestamp', (1399377810, 550176562))]

<Sniffed: TCP:14 UDP:0 ICMP:0 Other:0>

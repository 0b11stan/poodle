# Before openssl rebuild
```
root@batman:~# openssl s_client -connect catwoman:443
CONNECTED(00000003)
139746006050448:error:140790E5:SSL routines:SSL23_WRITE:ssl handshake failure:s23_lib.c:177:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 0 bytes and written 289 bytes
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : 0000
    Session-ID: 
    Session-ID-ctx: 
    Master-Key: 
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1609346988
    Timeout   : 300 (sec)
    Verify return code: 0 (ok)
---
root@batman:~# openssl s_client -connect catwoman:443 -ssl3
CONNECTED(00000003)
139881904932496:error:1409E0E5:SSL routines:SSL3_WRITE_BYTES:ssl handshake failure:s3_pkt.c:637:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 0 bytes and written 0 bytes
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : SSLv3
    Cipher    : 0000
    Session-ID: 
    Session-ID-ctx: 
    Master-Key: 
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1609347905
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
---
```

# After Openssl rebuild

```
root@batman:~# openssl s_client -connect catwoman:443      
CONNECTED(00000003)
140227804108432:error:14077102:SSL routines:SSL23_GET_SERVER_HELLO:unsupported protocol:s23_clnt.c:726:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 7 bytes and written 289 bytes
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : 0000
    Session-ID: 
    Session-ID-ctx: 
    Master-Key: 
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1609350184
    Timeout   : 300 (sec)
    Verify return code: 0 (ok)
---
root@batman:~# openssl s_client -connect catwoman:443 -ssl3
CONNECTED(00000003)
depth=0 CN = catwoman
verify return:1
---
Certificate chain
 0 s:/CN=catwoman
   i:/CN=catwoman
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDBzCCAe+gAwIBAgIUUzUL9khTt2GxSYH7oUMz22pg6RkwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIY2F0d29tYW4wHhcNMjAxMjMwMDk0NzI1WhcNMjEwMTI5
MDk0NzI1WjATMREwDwYDVQQDDAhjYXR3b21hbjCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBAMWSyPZ6UDTxHhgGwAOzU39heX+Ub9mNqZA79MOqQQyzrr5x
sZ8yN4b9auK1MDsizuyMCn6qSuLwYQBOJ/WeBer5IdcdZTOZiiT+Dqh3nIp6LRQt
FNqZQ4Cth5g1a/8NLSQjmtc8I5saFoVcrcGZlo+oW7aSwNfseakHAYZBnoWQq3qc
AwmE7C5NYZzXMvWws8sT6ULHzfDJ4A2ajjGQRgeOQRPLxxp9BeVrTe0+GHkPXmsA
9N9va/or9OsCELjLDc0ZdDRvzDGIMmL26wWoYi68+HLNZzu9LTuJN3agTzU/kCL7
G8sXzS40KEHzhv1cYbuG652msdcA8fp+PBSacVMCAwEAAaNTMFEwHQYDVR0OBBYE
FOfdv6hxsQgFeuKal8b78c3CLpvsMB8GA1UdIwQYMBaAFOfdv6hxsQgFeuKal8b7
8c3CLpvsMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAJmm13wN
LstDmaqpHMzkZk7To758U/XPE7PGRefg9BonagVMzkY40k4FC8rm/XvvSCSblXqE
Ik8gcHOe+7jtF8s24Dywj0eq4J89IpEIyq4b6CYEBhBTsqKCdOQWa13uXOCkiTXa
NPRbgX7nMFFF88iMbXFsR+t5wka+t08/nuJd9V6gSSo9U3mAKzHBGStxTRztfW+k
Nu9PBdSEygQgv3jttgKXWV3rSn0JytFOiVIT/9OKdlnHwLaHBe9AXESboJ2KkdkE
llc6QASPp+jprWpKLm4hIEvmZtR1Gk+GOy3W8P+XcPfakK/x2Yb2yu3rKIJRm/ge
7zY5koBKIhXU4es=
-----END CERTIFICATE-----
subject=/CN=catwoman
issuer=/CN=catwoman
---
No client certificate CA names sent
---
SSL handshake has read 1300 bytes and written 272 bytes
---
New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-SHA
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : SSLv3
    Cipher    : ECDHE-RSA-AES256-SHA
    Session-ID: DE46F43E6442C93177F66275D67DBDEE6E9102ABA6D63F1294CEB541F2669951
    Session-ID-ctx: 
    Master-Key: BBE4E777202B2598FC213CDAC32E76853D8ED4B51B26E6072D4D3DB06BF57E650D22CE43C9CB37195ECE0CB3ACB2C72D
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1609350193
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
---
```

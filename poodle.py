from scapy import *

load_layer('tls')

def compute(packet):
    if packet.flags == "PA":
        packet.show()

sniff(iface="eth1", filter="tcp", prn=lambda p: compute(p["TCP"]))

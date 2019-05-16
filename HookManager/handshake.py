from kamene.all import *
##from Scapy.all import *

class run:
    def execute(self, packet):
        if(packet.haslayer(TCP)):
            dst = packet.dst
            src = packet.src
            srcPort = packet.sport
            dstPort = packet.dport
            ack = packet.ack + 1 
            seq = packet.seq
            ip = IP(srrc = src, dst = dst)
            SYN = TCP(sport = srcPort, dport = dstPort, seq = seq, ack = ack)
            SYN_ACK = sr1(ip/SYN)


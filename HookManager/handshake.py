from kamene.all import *

class run:
    def execute(self, packet):
        dst = packet.dst
        src = packet.src
        srcPort = packet.sport
        dstPort = packet.dport

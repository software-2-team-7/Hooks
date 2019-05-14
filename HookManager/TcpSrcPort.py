from kamene.all import *

class TcpSrcPort:
    def changeTCPPort(self, packet):
        newPort = 55555
        if(packet.hasLayer(TCP)):
            packet.sport = newPort
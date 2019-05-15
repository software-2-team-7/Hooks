from kamene.all import *

class TcpSrcPort:
    def run(self, packet):
        newPort = 55555
        if(packet.hasLayer(TCP)):
            packet.sport = newPort

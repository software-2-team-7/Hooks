from kamene.all import *

class run:

    def __init__(self, packet):
        self.packet = packet
        print("Initialized.")


    def execute(self ):
        newPort = 55555
        if(self.packet.hasLayer(TCP)):
            self.packet.sport = newPort
        return self.packet
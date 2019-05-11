#! /usr/bin/env python3
from kamene.all import *
from netfilterqueue import NetfilterQueue
from Hook import Hook
from HookCollection import HookCollection

def modify(packet):
    testHook = Hook("Test",1,True,"Neat!",2,"testHook.py")
    hooks = []
    hc = HookCollection("testCollection",0,True,"Test hook coll.",hooks)
    hc.addHook(testHook)
    newpkt = hc.executeHookSequence(packet)

    pkt = IP(packet.get_payload()) #converts the raw packet to a scapy compatible string

    #modify the packet all you want here

    packet.set_payload(str(pkt)) #set the packet content to our modified version

    packet.accept() #accept the packet



nfqueue = NetfilterQueue()
#1 is the iptabels rule queue number, modify is the callback function
nfqueue.bind(1, modify) 
try:
    print ("[*] waiting for data")
    nfqueue.run()
except KeyboardInterrupt:
    pass

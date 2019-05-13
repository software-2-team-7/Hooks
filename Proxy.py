#! /usr/bin/env python3
from kamene.all import *
from netfilterqueue import NetfilterQueue
from HookManager.Hook import Hook
from HookManager.HookCollection import HookCollection
from rules import rules as rules
import sys
from io import BytesIO

def modify(packet):
    if rules.captureFilterStatus:
        testHook = Hook("Test",True,"Neat!",2,"testHook.py")
        hooks = []
        hc = HookCollection("testCollection",0,True,"Test hook coll.",hooks)
        hc.addHook(testHook)
        newpkt = hc.executeHookSequence(packet)


    pkt = IP(packet.get_payload()) #converts the raw packet to a scapy compatible string

    #pktAsB = bytes(pkt)
    
    #print(pktAsB)

    a = pkt.sprintf("%.time% %-15s,IP.src% -> %-15s,IP.dst% %IP.chksum% "
                    "%03xr,IP.proto% %r,TCP.flags%")

    for layer in pkt:
        print(layer.dst)

    packet.accept() #accept the packet



rule = rules()
#rule.enableFilter() To enable filter
rule.set()
nfqueue = NetfilterQueue()
#1 is the iptabels rule queue number, modify is the callback function
nfqueue.bind(1, modify)
try:
    print ("[*] waiting for data")
    nfqueue.run()
except KeyboardInterrupt:
    rule.flush()
    pass

#! /usr/bin/env python3
from kamene.all import *
from netfilterqueue import NetfilterQueue
from HookManager.Hook import Hook
from HookManager.HookCollection import HookCollection
from rules import rules as rules
from threading import Thread
from time import sleep

class Proxy(Thread):
	proxyStatus = False;
	def __init__(self):
		print("Proxy")
		self.proxyStatus = False;
		self.rule = rules()
		super().__init__()

	def modify(self, packet):
		if rules.captureFilterStatus:
			testHook = Hook("Test",True,"Neat!",2,"testHook.py")
			hooks = []
			hc = HookCollection("testCollection",0,True,"Test hook coll.",hooks)
			hc.addHook(testHook)
			newpkt = hc.executeHookSequence(packet)

		pkt = IP(packet.get_payload()) #converts the raw packet to a scapy compatible string

		pkt.summary()

		packet.accept() #accept the packet


	def run(self):
		print("running")
		#while(self.proxyStatus):
		#rule.enableFilter() To enable filter
		nfqueue = NetfilterQueue()
		nfqueue.bind(1, self.modify)
		#try:
		print ("[*] waiting for data")
		nfqueue.run()
		#except KeyboardInterrupt:

			#   pass

	def turnOn(self):
		self.rule.set()
		self.proxyStatus = True

	def turnOff(self):
		self.rule.flush()
		self.proxyStatus = False

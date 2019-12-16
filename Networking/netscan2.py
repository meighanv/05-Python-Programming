#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	print(arp_request.summary())
	

scan("10.0.2.2") # python3 issue 



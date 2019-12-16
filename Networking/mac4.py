#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "00:11:44:55:66:66"

print("Changing Mac Changer address: " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

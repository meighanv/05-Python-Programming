#!/usr/bin/env python

import subprocess

interface = "eth0"

print("Changing Mac Changer address: " + interface)

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:22:33:44:55:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)

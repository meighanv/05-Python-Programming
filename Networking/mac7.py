#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Interface to change mac address")
parser.add_option("-m","--mac", dest="new_mac", help="add the new mac address")

(options, arguments)=parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("Changing Mac Changer address: " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
subprocess.call(["ifconfig", interface, "up"])

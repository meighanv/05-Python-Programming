#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
	print("Changing Mac Changer address: " + interface + " to " + new_mac)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
	subprocess.call(["ifconfig", interface, "up"])
	subprocess.call(["ifconfig"])


def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface", dest="interface", help="Interface to change mac address")
	parser.add_option("-m","--mac", dest="new_mac", help="add the new mac address")
	return parser.parse_args()

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)




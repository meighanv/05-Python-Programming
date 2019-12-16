#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface", dest="interface", help="Interface to change mac address")
	parser.add_option("-m","--mac", dest="new_mac", help="add the new mac address")
	(options, arguments)= parser.parse_args()
	if not options.interface:
		# code to handle error
		parser.error(" Please specify an interface, use --hellp for more details")
	elif not options.new_mac:
		# code to handle error
		parser.error(" Please specify an new mac, use --hellp for more details")
	return options




def change_mac(interface, new_mac):
	print("Changing Mac Changer address: " + interface + " to " + new_mac)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
	subprocess.call(["ifconfig", interface, "up"])
	subprocess.call(["ifconfig"])





def get_current_mac(interface):

	ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("Could not read mac address: ")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print("Mac address was successfully changed to " + current_mac)
else:
	print("MAC address did not change.")












#!/usr/bin/env python

# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

import socket

def get_remote_machine_info():
    remote_host = 'www.dakjldksajkj.org'
    try:
        print ("IP address of %s: %s" %(remote_host, socket.gethostbyname(remote_host)))
    # There are situations where even nonsensical domains will be 
    # redirected by the ISP when a valid suffix is provided which will
    # return an IP that actually points to something like DNSSearch.com 
    # or an ISP webpage 
    except socket.error as err_msg:
        print ("%s: %s" %(remote_host, err_msg))

if __name__ == '__main__':
    get_remote_machine_info()
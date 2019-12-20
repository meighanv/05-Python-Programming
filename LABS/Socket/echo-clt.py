#!/usr/bin/env python 

# This program is optimized for Python 2.7.12 and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket 
import sys 
 
import argparse 
 
host = 'localhost' 
 
def echo_client(port): 
    """ A simple echo client """ 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    try:
        sock.connect(server_address) 
    except ConnectionRefusedError as e:
        print(f"Bad Address or Port: {e}")
        return
    # Send data 
    try: 
        # Send data 
        message = "Test message. This will be echoed" 
        print ("Sending %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Received: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 
     
# This allows the function to execute if the python file is executed directly
# This means that the function will have to be called directly if imported
if __name__ == '__main__': 
    # This series of statements allows for in-line arguments
    parser = argparse.ArgumentParser (description='Socket Server Example') 
    parser.add_argument('--port', action="store", dest="port", type=int, required=True) 
    # This was testing how to add additional, optional arguments
    parser.add_argument('--welcome', action="store", dest="welcome", type=str, required=False)
    given_args = parser.parse_args()  
    port = given_args.port 
    msg = given_args.welcome
    # Executes if the welcome message option is used
    if msg:
        print(msg)
    echo_client(port)
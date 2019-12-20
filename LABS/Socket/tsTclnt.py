#!/usr/bin/env python
from socket import *
import pickle
import argparse

def client_conn(HOST, PORT):
    BUFSIZ = 2048
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    try:
        tcpCliSock.connect(ADDR) 
    except ConnectionRefusedError as e:
        print(f"Bad Address or Port: {e}")
        return

    while True:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(data.encode())
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        result = pickle.loads(data)
        if isinstance(result, list):
            for i in result:
                print(i)
        else:
            print(result)

    tcpCliSock.close()

if __name__ == '__main__': 
    # This series of statements allows for in-line arguments
    parser = argparse.ArgumentParser (description='TCP Socket Client Example') 
    parser.add_argument('--port', action="store", dest="port", type=int, required=True) 
    # This was testing how to add additional, optional arguments
    parser.add_argument('--host', action="store", dest="host", type=str, required=True)
    given_args = parser.parse_args()  
    port = given_args.port 
    host = given_args.host

    client_conn(host, port)
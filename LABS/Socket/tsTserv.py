#!/usr/bin/env python

from socket import *
from time import ctime
import pickle
import os

def oscommand(data, client):
    if data.decode() == 'date':
        result = pickle.dumps(ctime())
        client.send(result)
    elif data.decode() == 'os':
        result = pickle.dumps(os.name)
        client.send(result)
    elif data.decode() == 'ls':
        result = pickle.dumps(os.listdir())
        client.send(result)
    elif data.decode().lower() == 'exit':
        return 'exit'
    else:
        client.send(b'I would love to have a conversation, but I am not equipped for that. Please try \'os\', \'ls\', or \'date\'')
    

HOST = ''
PORT = 21567
BUFSIZ = 2048
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        print(type(data))
        if not data:
            break
        #tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())
        action = oscommand(data, tcpCliSock)
        if action == 'exit':
            exit()
    tcpCliSock.close()
tcpSerSock.close()


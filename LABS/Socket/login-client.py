from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = 'localhost'  # on same host
PORTNUMBER = 11267      # same port number
BUFFER = 80             # size of the buffer

SVR = (HOSTNAME, PORTNUMBER)
CLT = Socket(AF_INET, SOCK_STREAM)
CLT.connect(SVR)

print('player is ready to guess')
while True:
    GUESS = input('Password: ')
    CLT.send(GUESS.encode())
    ANSWER = CLT.recv(BUFFER).decode()
    print('>', ANSWER)
    if 'GOLD' in ANSWER:
        break

CLT.close()
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = 'localhost'  # on same host
PORTNUMBER = 11267      # same port number
BUFFER = 80             # size of the buffer

DEALER = (HOSTNAME, PORTNUMBER)
PLAYER = Socket(AF_INET, SOCK_STREAM)
PLAYER.connect(DEALER)

print('player is ready to guess')
while True:
    GUESS = input('Give number : ')
    PLAYER.send(GUESS.encode())
    ANSWER = PLAYER.recv(BUFFER).decode()
    print('>', ANSWER)
    if ANSWER == 'found the secret':
        break

PLAYER.close()
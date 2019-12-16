from random import randint
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = ''       # blank so any address can be used
PORTNUMBER = 11267  # number for the port
BUFFER = 80         # size of the buffer

DEALER_ADDRESS = (HOSTNAME, PORTNUMBER)
DEALER = Socket(AF_INET, SOCK_STREAM)
DEALER.bind(DEALER_ADDRESS)
DEALER.listen(1)

print('dealer waits for player to connect')
PLAYER, PLAYER_ADDRESS = DEALER.accept()
print('dealer accepted connection request from ',\
    PLAYER_ADDRESS)

SECRET = randint(0, 9)
print('the secret is %d' % SECRET)

while True:
    print('dealer waits for a guess')
    GUESS = PLAYER.recv(BUFFER).decode()
    print('dealer received ' + GUESS)
    if int(GUESS) < SECRET:
        REPLY = 'too low'
    elif int(GUESS) > SECRET:
        REPLY = 'too high'
    else:
        REPLY = 'found the secret'
    PLAYER.send(REPLY.encode())
    if REPLY == 'found the secret':
        break

DEALER.close()
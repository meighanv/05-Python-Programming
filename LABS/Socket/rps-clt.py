from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = 'localhost'  # on same host
PORTNUMBER = 11267      # same port number
BUFFER = 80             # size of the buffer

DEALER = (HOSTNAME, PORTNUMBER)
PLAYER = Socket(AF_INET, SOCK_STREAM)
PLAYER.connect(DEALER)

choices = [0, 1, 2]

print('Let\'s play Rock, Paper, Scissors!')
while True:
    GUESS = -1
    while int(GUESS) not in choices:
        GUESS = input('Select 0 for Rock, 1 for Paper, 2 for Scissors: ')
    PLAYER.send(GUESS.encode())
    ANSWER = PLAYER.recv(BUFFER).decode()
    print('>', ANSWER)
    if ANSWER != 'TIE':
        break

PLAYER.close()
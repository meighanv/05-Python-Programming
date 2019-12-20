from random import randint
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

def playGame(PLAYER, BUFFER):
    choices = ['Rock', 'Paper', 'Scissors']

    while True:
        CHOICE = randint(0, 2)
        print(f'Computer has chosen: {CHOICE}')
        print('Computer waits for user\'s choice...')
        GUESS = PLAYER.recv(BUFFER).decode()
        print(f'User\'s choice: {choices[int(GUESS)]}')
        user_wins = 'User\'s ' + choices[int(GUESS)] + ' beats Computer\'s ' + choices[int(CHOICE)]
        comp_wins = 'Computer\'s ' + choices[int(CHOICE)] + ' beats User\'s ' + choices[int(GUESS)]
        # 'User wins' scenarios
        if int(GUESS) == 0 and int(CHOICE) == 2:
            REPLY = user_wins 
            PLAYER.send(REPLY.encode())
            break
        elif int(GUESS) == 1 and int(CHOICE) == 0:
            REPLY = user_wins
            PLAYER.send(REPLY.encode())
            break
        elif int(GUESS) == 2 and int(CHOICE) == 1:
            REPLY = user_wins
            PLAYER.send(REPLY.encode())
            break
        # 'Computer wins' scenarios
        elif int(CHOICE) == 0 and int(GUESS) == 2:
            REPLY = comp_wins
            PLAYER.send(REPLY.encode())
            break
        elif int(CHOICE) == 1 and int(GUESS) == 0:
            REPLY = comp_wins
            PLAYER.send(REPLY.encode())
            break
        elif int(CHOICE) == 2 and int(GUESS) == 1:
            REPLY = comp_wins
            PLAYER.send(REPLY.encode())
            break
        else:
            REPLY = 'TIE'
        PLAYER.send(REPLY.encode())

def main():
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

    playGame(PLAYER, BUFFER)

    DEALER.close()

main()
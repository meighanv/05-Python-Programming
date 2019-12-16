from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = ''       # blank so any address can be used
PORTNUMBER = 11267  # number for the port
BUFFER = 80         # size of the buffer

SVR_ADDRESS = (HOSTNAME, PORTNUMBER)
SVR = Socket(AF_INET, SOCK_STREAM)
SVR.bind(SVR_ADDRESS)
SVR.listen(1)

print('Waiting for client to connect')
CLT, CLT_ADDRESS = SVR.accept()
print('Connection from ',\
    CLT_ADDRESS)

SECRET = ['password', 'whodey', 'winning', 'jamaica']
# print('the secret is %d' % SECRET)

while True:
    print('Please provide your password:')
    GUESS = CLT.recv(BUFFER).decode()
    # print('dealer received ' + GUESS)
    if GUESS not in SECRET:
        REPLY = 'Access Denied'
    else:
        REPLY = 'Access Granted. You have access to the GOLD!!!'
    CLT.send(REPLY.encode())
    if REPLY == 'Access Granted. You have access to the GOLD!!!':
        break

SVR.close()
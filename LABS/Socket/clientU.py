from socket import *

def main():
    host = 'localhost'

    sock = socket(AF_INET, SOCK_DGRAM)
    addr = (host,9898)
    
    msg = b"What happened?!?\n"
    sock.sendto(msg, addr)
    sock.close()

main()
from socket import *

def main():
    host = 'localhost'

    sock = socket(AF_INET6, SOCK_STREAM)
    addr = (host,9898)
    sock.connect(addr)

    try:
        msg = b"This was a terrible test!\n"
        sock.sendall(msg)
    except socket.errno as e:
        print("Socket error ", e)
    finally:
        sock.close()

main()
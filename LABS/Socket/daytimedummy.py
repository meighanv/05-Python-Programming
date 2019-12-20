from socket import *
def main():
    host = '129.6.15.26'

    sock = socket(AF_INET, SOCK_STREAM)
    addr = (host,13)
    
    msg = b"What happened?!?\n"
    sock.connect(addr)
    sock.send(msg)
    while True:
        data = sock.recv(512)
        if data:
            print(data.decode())
        else:
            break
    sock.close()

main()
# This is the code for the server side
from socket import *
size = 512
host = ''
port = 9898

# Create server socket
s = socket(AF_INET6, SOCK_STREAM)
s.bind((host, port))
s.listen(5)
c,a = s.accept()
data = c.recv(size)

if data:
    f = open("storage.dat", '+w')
    print("connection from: ", a[0])
    f.write(a[0])
    f.write(":")
    f.write(data.decode("utf-8"))
    f.close()
s.close()

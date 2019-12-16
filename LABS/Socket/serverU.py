# This is the code for the server side
from socket import *
size = 512
host = ''
port = 9898

# Create server socket
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

c,a = s.recvfrom(size)
data = c 
# print(c)

if data:
    f = open("storageUDP.dat", '+w')
    print("connection from: ", a[0])
    f.write(a[0])
    f.write(":")
    f.write(data.decode("utf-8"))
    f.close()
   
s.close()

import socket 
 
def find_service_name(): 
    protocolname = 'udp' 
    for port in range(1,1000): 
        try:
            print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))) 
        except OSError:
            pass
    print("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))) 


if __name__ == '__main__': 
    find_service_name() 
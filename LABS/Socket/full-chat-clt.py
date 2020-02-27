from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import argparse

# Setting Global constant for buffer size
BUFSIZ = 1024

# Defining Main
def main():    end
    # Creating a thread for receiving chat data; pointing it to the 
    # receive function.
    receive_thread = Thread(target=receive)
    # Starting the thread
    receive_thread.start()

    # Creating a thread for sending
    send_thread = Thread(target=send)
    # Starting the thread for sending
    send_thread.start()

def receive():
    #Handles receiving of messages.
    while True:
        try:
            # reads what the sicket has received and prints to client screen
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(msg)
        except OSError:  # Possibly client has left the chat.
            break


def send():  
    while True:
        #Handles sending of messages
        msg = input('\n>')
        # Sends the input as bytes with UTF-8 encoding over the socket
        client_socket.send(bytes(msg, "utf8"))
        # Checks the input to determine if the user has decided to quit
        if msg == "{quit}":
            # If the user has quit, close connex and exit program
            client_socket.close()
            exit()

# Creating the client connection and returning socket to main
def client_conn(host, port):
    # Setting the address tuple w/ in-line args
    ADDR = (host, port)

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(ADDR)
    return sock



if __name__ == '__main__': 
    # This series of statements allows for in-line arguments
    parser = argparse.ArgumentParser (description='TCP Chat Client Example') 
    # Client parameter
    parser.add_argument('--port', action="store", dest="port", type=int, required=True) 
    # Host parameter
    parser.add_argument('--host', action="store", dest="host", type=str, required=True)
    given_args = parser.parse_args()  
    port = given_args.port 
    host = given_args.host

    # Calling client_conn to create the client socket
    client_socket = client_conn(host, port)
    # call Main
    main()
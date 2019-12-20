#!/usr/bin/env python3
#Server for multithreaded (asynchronous) chat application.
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    #Sets up handling for incoming clients.
    while True:
        client, client_address = SERVER.accept()
        print(f"{client_address}:{client_address} has connected.")
        # Send greeting upon successful connection
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        # Adding to the addresses dictionary
        addresses[client] = client_address
        # Create and start the thread calling the handle_client function
        # and the necessary arguments  
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    #Handles a single client connection.
    # Set name to info in the socket buffer from the response from
    # the prompt in accept_incoming_connections 
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    # Welcoming the user
    client.send(bytes(welcome, "utf8"))
    # Creating the msg for broadcast
    msg = "%s has joined the chat!" % name
    # Calls broadcast function to send message to all users
    broadcast(bytes(msg, "utf8"))
    # Adding the name to the clients dictionary with the socket 
    # as the key
    clients[client] = name

    # Loop to continue broadcasting new messages
    while True:
        # Setting mesg to broadcast
        msg = client.recv(BUFSIZ)
        # as long as the message is not {quit}
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        # if it is {quit} then close connection and notify other users
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            # Remove the quitting client
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

# prefix is for name identification.
def broadcast(msg, prefix=""):  
    # Broadcasts a message to all the clients.
    # Iterate through each socket in the clients dictionary to send msg
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
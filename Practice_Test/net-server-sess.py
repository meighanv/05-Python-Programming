#!/usr/bin/env python

"""
Create a shared session keys Client Server application according to the following specifications:

*   Both the Server and the Client share a list of 10 session keys, where each key is 128 bits

*   After a successful connection setup between the server and the client, the server randomly picks
    one session key, and masks this key using XOR operation with a random value R of 128 bits

*   The server sends the masked value to the client,
    which will try to figure out which session key has been selected by the server.
    The Client will do the following:
     -  Randomly select a key from the session key list
     -  Apply XOR operation with the masked value received from the server to obtain a random value R'
     -  Send R' to the server
     -  The server compares its random value R with R' received from the client.
        #   if there is a match, then the client has picked the same session key,
            and the server will send "SUCCESS" message to the client,
            which will then display the session key and close the connection with the server
        #   If there is no match, the server will send "INVALID KEY: x more trail(s)",
            where x is the number of remaining trails that the client can do.
            In total, the client has 3 trails to guess the session key selected by the server.
            If the client consumed the 3 trails without getting the session key, the sever will send "UNAUTHORIZED CLIENT",
            and terminate the connection with the client.

*   Note the following:
    -   The server is running forever
    -   The server displays the IP address of the client connecting to it
    -   After a successful connection setup between the server and the client,
        the server send a message "SERVER>>> Connection successful" to the client,
        which will be displayed on the client side
    -   The server messages: "SUCCESS", "INVALID KEY: x more trail(s)" , and "UNAUTHORIZED CLIENT"
        are displayed on the client side
    -   "Connection terminated" message is displayed on both the client and the server sides
         when the client-server connection is terminated
    -   You can run the client program many times, this will ***simulate*** that different clients are connecting to the server.
        One run for the client program may end up with "UNAUTHORIZED CLIENT" while another run may end up with "SUCCESS"

"""
import socket, random, string, struct, sys, threading, logging
from random import randint
from threading import Thread

# ------------------------set logging configs -----------
# https://docs.python.org/2/library/logging.html?highlight=logging#module-logging 
# https://realpython.com/python-logging/#the-logging-module
logging.basicConfig(
    filename =  'serverOuput.log', 
    filemode =  'w', 
    format =    '%(process)d ---- %(levelname)s ---- %(message)s',
    level =     logging.INFO  # will log anything greater than the level specified here
    )


failureXML = """<?xml version="1.0" encoding="UTF-8"?>
<testsuite errors="0" failures="1" name="Networking-Socket" tests="1" time="0.000">
<testcase classname="Networking-Socket" name="find_key_requests" time="0.000">
<failure message="Incorrect"></failure>
</testcase>
</testsuite>"""

successXML = """<?xml version="1.0" encoding="UTF-8"?>
<testsuite errors="0" failures="0" name="Networking-Socket" tests="1" time="0.000">
<testcase classname="Networking-Socket" name="find_key_requests" time="0.000"/>
</testsuite>"""

serverHOST = "0.0.0.0"
serverPort = 5000
session_keys = ["aa072fbbf5f408d81c78033dd560d4f6",
                "bb072fbbf5f408d81c78033dd560f6d4",
                "f5072fbbf5f408d81c78033dd5f6d460",
                "408df5072fbbf5f81c3dd5f6d4607803",
                "dd5f408df5072fbbfc36d46078035f81",
                "c36d408df5072fbbf46078035f81dd5f",
                "35f8c36df5072fbbf4607801dd5fd408",
                "2f07aaf408d81c78033dd560d4f6bbf5",
                "80332ff408d81c7dd560d4f6bbf507aa",
                "560d4f8033281c7dd6bbf507aaff408d",
               ]

g_evt = threading.Event()


def signaled():
    return g_evt.isSet()


def doWork(sock):
    while not signaled():

        try:
            connection, address = sock
            connection.settimeout(5)
            print("Connection received from: {}".format(address[0]))
            logging.info("Connection received from: {}".format(address[0]))

            # =========================================================================
            # no longer setting key using the client's IP, hardcoding the key here
            # ---------------------------------------------------------------------
            # array = address[0].split('.')
            # key_index = list(str(int(array[3])))
            # key_index = key_index[-1]
            key_index = 5
            # =========================================================================

            # step 5: send and receive data via connection
            connection.send("SERVER>>> Connection successful".encode())
            serverRandomValue = ''.join([random.choice("abcdef" + string.digits) for n in range(32)])
            xValue = hex(int(session_keys[int(key_index)], 16) ^ int(serverRandomValue, 16)).rstrip("L")
            connection.send(xValue.encode())
            print("Server sent {}".format(xValue))
            logging.info("Server sent {}".format(xValue))
            # print >> sys.stderr, "session_key is: ", session_keys[int(key_index)]
            # print >> sys.stderr, "xValue is: ", xValue

            clientRandomValue = connection.recv(1024)  # 1024 is the buffer size
            print("Server recieved {}".format(clientRandomValue))
            logging.info("Server recieved {}".format(clientRandomValue))
            clientRandomValue = int(clientRandomValue, 16)
            serverRandomValue = int(serverRandomValue, 16)
            if(clientRandomValue == serverRandomValue):
                connection.send("Success! You found the key: \n{0}\n".format(successXML).encode())
                print("Success! You found the key")
                logging.info("Success! You found the key")
                #print >> sys.stderr, "SUCCESS on ip number: ", address[0]
                break
            else:
                ## ENCODE ORIGINALLY MISSING CREATING BYTES OBJECT ISSUE
                connection.send("INVALID KEY\n{0}\n".format(failureXML).encode()) 
                print("FAILURE, invalid key received")
                logging.info("FAILURE, invalid key received")
                # print >> sys.stderr, "clientRandomValue: ", clientRandomValue
                # print >> sys.stderr, "serverRandomValue: ", serverRandomValue
            print("\n\n")
        except Exception as e:
            connection.send("ERROR FROM SERVER:\n{0}".format(e).encode())
            print("Exception:")
            print(e)
            logging.error(e)
            break


def main():
    # step 1: create socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    workers = []

    try:
        # step 2: bind the socket to address
        serverSocket.bind((serverHOST, serverPort))
        # step 3: wait for connection request
        serverSocket.listen(10)
        print("Server waiting for connection on port 5000...")
        logging.info("Server waiting for connection on port 5000...")
        #print "Server waiting for connection on port 5000..."
        while True:
            # step 4: establish connection for request
            sock = serverSocket.accept()
            t = Thread(target=doWork, args=(sock,))
            t.daemon = True
            t.start()
            workers.append(t)

    except socket.error as e:
        print("Call to bind failed")
        logging.error("Call to bind failed")
        print(str(e))
        logging.error(str(e))

    except KeyboardInterrupt:
        print("Caught Ctrl-C, signaling worker threads to exit")
        logging.warning("Caught Ctrl-C, signaling worker threads to exit")
        g_evt.set()
        for t in workers:
            t.join()
    finally:
        serverSocket.close()


if __name__=='__main__':
    main()

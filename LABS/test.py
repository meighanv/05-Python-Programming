import pickle
from os import path 

filename = 'email.dat'

def readBinary(filename):
    email_file = open(filename, 'rb')
    end_of_file = False
    while not end_of_file:
        try:
            #unpickle next object
            dictionary = pickle.load(email_file)
            return dictionary
        except EOFError:
            #Set flag to indicate EOF reached
            end_of_file = True
    email_file.close()
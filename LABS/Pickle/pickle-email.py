"""
​
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the dictionary from the file and unpickle it.
​
"""
import pickle 
from os import path

#define main
def main():
    #output_file = open('email.dat', 'wb')
    
    #List of valid menu options
    menuOptions = ['l','m','a','d','x']
    #setting filename variable for check
    filename = 'email.dat'
    #Checking for existence of file; if it's missing it will create prompting for first entry
    if path.exists(filename) == False:
        freshStart(filename)
        
    #Init selection for while loop
    selection = 'b'
    while selection.lower() != 'x':
        selection = menu(menuOptions)
        #lowers the input of to match against selections
        if selection.lower() == 'l':
            lookupEntry(filename)
        elif selection.lower() == 'm':
            modEntry(filename)
        elif selection.lower() == 'a':
            addEntry(filename)
        elif selection.lower() == 'd':
            removeEntry(filename)
        elif selection.lower() == 'x':
            #Print exit message
            print('Good bye!')
        else:
            #Print error message if input doesn't match option
            print('Incorrect Selection')

#This function is meant to address the first use of the program where the email file doesn't exist
def freshStart(filename):
    #Opens filename in binary write mode
    email_file = open(filename, 'wb+')
    #Create empty dictionary
    email_dict = {}
    #Let's the user know why they are being prompted for initial entries
    print('The file {} is not detected. Starting fresh; please provide the first entry: '.format(filename))
    #Prompts for initial entry
    email_dict.update({(input('Name: ')).lower(): (input('Email: ')).lower()})
    #writes dictionary to binary file
    pickle.dump(email_dict, email_file)
    #close file
    email_file.close()

def menu(options):
    #Printing program menu
    print('PROGRAM MENU')
    print('E-mail Lookup (press L)')
    print('Add an entry (press A)')
    print('Modify an entry (press M)')
    print('Delete an entry (press D)')
    print('EXIT (press X)')   
    print('\n\n') 
    # Getting user input for menu option
    selection = input('What would you like to do?') 
    # Input validation for menu selection
    while selection.lower() not in options:
        selection = input('Invalid selection. What would you like to do?\n')
    print('\n')
    return selection
    

#Function to add entry to existing binary data file
def addEntry(filename):
    # Calling the readBinary function to read in the file as a dictionary
    email_dict = readBinary(filename)
    #Prompts for entry
    email_dict.update({(input('Name: ')).lower(): (input('Email: ')).lower()})
    #Opens the file on disk for writing
    email_file = open(filename, 'wb')
    #Dump data to file
    pickle.dump(email_dict, email_file)
    #close file
    email_file.close()

def modEntry(filename):
    # Calling the readBinary function to read in the file as a dictionary
    email_dict = readBinary(filename)
    # Print keys as options
    print('Names\n-----------')
    for i in email_dict:
        print(i)
    # Gets user input for entry they wish to change
    query = input('Provide the name from above to change:\n')
    # Prompts for email entry to modify
    email_dict.update({query.lower(): (input('Email: ')).lower()})
    # Opens the file on disk for writing
    email_file = open(filename, 'wb')
    # Dump data to file
    pickle.dump(email_dict, email_file)
    # close file
    email_file.close()

def lookupEntry(filename):
    # Calling the readBinary function to read in the file as a dictionary
    email_dict = readBinary(filename)
    # Gets user input for entry they wish to lookup
    query = input('Provide the name to lookup:\n')
    # Prints the email for the query or lets them know it's not found
    print(email_dict.get(query.lower(), 'Name not found'))
    print()

def removeEntry(filename):
    # Calling the readBinary function to read in the file as a dictionary
    email_dict = readBinary(filename)
    # Print keys as options for removal
    print('Names\n-----------')
    for i in email_dict:
        print(i)
    # Gets user input for entry they wish to lookup
    query = input('Provide the name to remove:\n')
    # Deletes entry from  dictionary
    del email_dict[query]
    # Verifies to the user that the entry was removed
    print(email_dict.get(query.lower(), 'Information successfully removed.\n'))
    print()
    # Opens the file on disk for writing
    email_file = open(filename, 'wb')
    # Dump data to file
    pickle.dump(email_dict, email_file)
    # close file
    email_file.close()

def readBinary(filename):
    # Opening the file in read mode
    email_file = open(filename, 'rb')
    # Setting EOF to false
    end_of_file = False
    #Setting while loop to get each object in binary file
    while not end_of_file:
        try:
            #unpickle next object
            dictionary = pickle.load(email_file)
            return dictionary
        except EOFError:
            #Set flag to indicate EOF reached
            end_of_file = True
    email_file.close()


main()
    
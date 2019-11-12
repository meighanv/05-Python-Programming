#serializing objects is the process of converting an object to a ....
#stream of bytes that can be saved to a file for later retreival. 
#This is called pickling in python.
#Good for transferring data, sending RPCs, sending things through a network; not human readable
# the 'b' in fileo-io modes is binary format which is used for pickling

""" 
output_file = open('mydata.dat','wb')
pickle.dump(object, file) 
"""
#This program demos object pickling
import pickle

#main function
def main():
    #Controls loop repetition
    again = 'y'

    #open a file for binary writing
    output_file = open('information.dat', 'wb')

    #Get data until user quits
    while again.lower() == 'y':
        #Get data on person and save it
        save_data(output_file)

        #Check for more user data
        again = input('Enter more data? (y/n): ')

    #close the file
    output_file.close()

#The save_data function gets data about a poerson
# stores it in a directory, and then pickles the
# dictionary to the specified file
def save_data(file):
    #Create empty dict
    person = {}

    #Get data for a person
    #person['name'] = input('Name: ')
    #person['age'] = input('Age: ')
    #person['weight'] = input('Weight: ')

    person.update({'name': input('Name: '), 'age', input('Age: '), 'weight', float(input('weight: ')) })
    
    #Pickle the dictionary
    pickle.dump(person, file)

#Call main
main()
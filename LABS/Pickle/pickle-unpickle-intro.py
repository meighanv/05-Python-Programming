#Demo object unpickling
import pickle

#main function
def main():
    #Indicate end of the file
    end_of_file = False

    #open a file for binary writing
    input_file = open('information.dat', 'rb')
    
    #read to end of file
    while not end_of_file:
        try:
            #unpickle next object
            person = pickle.load(input_file)

            #Display data
            display_data(person)

        except EOFError:
            #Set flag to indicate EOF reached
            end_of_file = True
    
    #close the file
    input_file.close()

#This function displays the person data in the dict
# that is passed as an arg
def display_data(person):
    print('Name: ', person['name'])
    print('Age: ', person['age'])
    print('Weight: ', person['weight'])
    print()

#Call main
main()
from os import path
import employee as e
import pickle

def main():
    # Calls the function to unpickle file data for usage 
    # in the dictionary
    filename = 'employee.dat'
    if path.exists(filename):
        emp_dict = readData(filename)
    else:
        print('\nNo employee database found. Starting fresh....\n')
        emp_dict = {}
    
    # Presents menu and returns the selection
    selection = menu()
    while selection != 'x':
        # Takes the selection and executes the operation on the dictionary
        execute(selection, emp_dict)

        # Writes data to disk
        writeData(emp_dict, filename)

        # Reads data back in to refresh the dictionary
        emp_dict = readData(filename)

        # Next selection
        selection = menu()

def menu():
    #Setting options list
    options = ['l','m','a','d','x']
    #Printing program menu
    print('PROGRAM MENU')
    print('Employee Lookup (press L)')
    print('Add an employee entry (press A)')
    print('Modify an employee entry (press M)')
    print('Delete an employee entry (press D)')
    print('EXIT (press X)')   
    print('\n\n') 
    # Getting user input for menu option
    selection = input('What would you like to do?') 
    # Input validation for menu selection
    while selection.lower() not in options:
        selection = input('Invalid selection. What would you like to do?\n')
    print('\n')
    return selection

def readData(filename):
    # Opening the file in read mode
    emp_file = open(filename, 'rb')
    # Setting EOF to false
    end_of_file = False
    #Setting while loop to get each object in binary file
    while not end_of_file:
        try:
            #unpickle next object
            dictionary = pickle.load(emp_file)
            return dictionary
        except EOFError:
            #Set flag to indicate EOF reached
            end_of_file = True
    emp_file.close()

def writeData(dictionary, filename):
    #Opens the file on disk for writing
    emp_file = open(filename, 'wb')
    #Dump data to file
    pickle.dump(dictionary, emp_file)
    #close file
    emp_file.close()

def addEntry(dictionary):
    emp = e.Employee()
    emp.set_name()
    emp.set_id()
    emp.set_dept()
    emp.set_title()
    dictionary.update({emp.get_id(): emp})
    
def modEntry(dictionary):
    # Print keys as options
    print('Names\n-----------')
    for i in dictionary:
        print(f'\n{dictionary[i].get_id()}:\t{dictionary[i].get_name()}\n')
    # Gets user input for entry they wish to change
    query = input('Provide the ID from above to change:\n')
    # Prompts for email entry to modify
    emp = dictionary[query]
    emp.set_name()
    emp.set_dept()
    emp.set_title()
    dictionary.update({query: emp})
    
def lookupEntry(dictionary):
    # Gets user input for entry they wish to lookup
    query = input('Provide the ID to lookup:\n')
    # Prints the email for the query or lets them know it's not found
    result = dictionary.get(query, 'Employee ID not found')
    if result != 'Employee ID not found':
        print(f'\nEmployee Information:\n{dictionary[query].get_id()}\n{dictionary[query].get_name()}\n{dictionary[query].get_dept()}\n{dictionary[query].get_title()}\n\n')
    else:
        print('****Employee ID not found****')
    print()
    
def removeEntry(dictionary):
    # Print keys as options for removal
    print('ID\\Names\n-----------')
    for i in dictionary:
        print(f'{dictionary[i].get_id()}\n{dictionary[i].get_name()}\n\n')
    # Gets user input for entry they wish to lookup
    query = input('Provide the ID to remove:\n')
    # Deletes entry from  dictionary
    del dictionary[query]
    # Verifies to the user that the entry was removed
    print(dictionary.get(query, '\n****Information successfully removed.****\n'))
    print()

def execute(selection, dictionary):
    if selection.lower() == 'a':
        addEntry(dictionary)
    elif selection.lower() == 'm':
        modEntry(dictionary)
    elif selection.lower() == 'l':
        lookupEntry(dictionary)
    elif selection.lower() == 'd':
        removeEntry(dictionary)


# Calling main
main()
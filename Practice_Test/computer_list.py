'''
Write the function create_computer_objects that will read data from a file to 
create one or more computer objects and store one or more of these objects in a list.
 
Each valid object will be stored in the list in the order the data is read from the file.
The Computer class used to create the objects is defined in the supportClass.py file. 

Objects should be created with cost as a float, and ramGB/storageGB as integer

The function receives one parameter which is the name of the file. 
Each line in the file will be in the format of: brand, model, cost, ram, storage

Example:  Lenovo, Super Duper, 795.95, 16, 512
 
Only the following computers should have objects created and stored in the list:
- all brands except Asus, and
- cost greater than $500.00 and less than $1000, and
- 8 or more GB of ram

If a file cannot be opened, the function will return the string "FILE CORRUPTED"
If any of the cost, ram, or storage are invalid numbers, or any line in the file contains less
or more than the five required items, the function will return the string "INVALID DATA"

After the file is processed successfully, the function will return the list of objects.

'''

# Importing the class for computer
from supportClass import * 

# defining the function to create computer objects from file
def create_computer_objects(fileName):
    # Try opening file with exception handling if file unable to be found or read
    try:
        f = open(fileName, 'r')
        a = f.readlines()
        f.close()
    except FileNotFoundError:
        return f"FILE CORRUPTED"

    # creating empty list to store computer objects
    compList = []

    # Iterating through each line read from file
    for i in a:
        # splitting list on ", " which is expected format of the text file
        lineList = i.split(", ")

        # checking for valid count of line elements based on split
        if len(lineList) != 5:
            # Inform user data is invalid
            return f"INVALID DATA"
        
        # Storing each line element based on expected order
        brand = lineList[0]
        model = lineList[1]
        # Trying to convert cost, ram, storage into appropriate data types 
        try:
            cost = float(lineList[2])
            ramGB = int(lineList[3])
            storageGB = int(lineList[4])
        #if any of the conversions fail, inform user of invalid data
        except ValueError:
            return f"INVALID DATA"
        #create the computer object
        comp = Computer(brand, model, cost, ramGB, storageGB)
        
        # Add computer objects to list that meet prompt requirements
        if (comp.brand not in ['Asus','asus'] and (comp.cost > 500 and comp.cost < 1000) and comp.ramGB >= 8):
            compList.append(comp)

    #return the list         
    return compList

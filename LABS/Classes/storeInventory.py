import retailItem
import pickle

filename = 'inventory.dat'

def main():
    # Initialize object storage list
    inventory = []

    # Iterate for input of data for 3 retail items
    for i in range(3):
        item = retailItem.RetailItem()
        item.set_desc()
        item.set_unitCount()
        item.set_price()
        inventory.append(item)
        # Print visual assistance line
        print()
    
    # Print header for item listing
    print('\tDescription:\tUnits in Inventory:\tPrice:')
    # Iterate through the count of items such that the iterator 
    # variable of item can be used for counter for item
    # number labeling
    for item in range(len(inventory)):
        print(f'Item#{item+1}\t{inventory[item].get_desc()}\t\t{inventory[item].get_unitCount()}\t\t{inventory[item].get_price()}')

    writeData(inventory, filename)


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

def writeData(data, filename):
    #Opens the file on disk for writing
    q_file = open(filename, 'wb')
    #Dump data to file
    pickle.dump(data, q_file)
    #close file
    q_file.close()

main()
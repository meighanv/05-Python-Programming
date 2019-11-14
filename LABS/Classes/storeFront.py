# Still need to add clear register function

import retailItem
import cashregister
import pickle

def main():
    inv_file = 'inventory.dat'
    inventory = readData(inv_file)
    register = cashregister.CashRegister()

    keepGoing = ''
    while keepGoing.upper() != 'N':
        selection = -1
        printInv(inventory)
        while int(selection) not in range(1,len(inventory)+1):
            selection = input('Make a selection by choosing the item number:')
        addCart(selection, inventory, register)
        keepGoing = input('Add another item? (Y/N)')
        options = ['Y','N']
        while keepGoing.upper() not in options:
            keepGoing = input('Add another item? (Y/N)')
    register.set_total()
    print('Total purchase:\n${:.2f}'.format(register.get_total()))
        

        

def printInv(inventory):
    print('\tDescription:\tUnits in Inventory:\t\tPrice:')
    for item in range(len(inventory)):
        print(f'Item#{item+1}\t{inventory[item].get_desc()}\t\t{inventory[item].get_unitCount()}\t\t{inventory[item].get_price()}')

def addCart(selection, inventory, register):
    item = retailItem.RetailItem()
    desc = inventory[int(selection)-1].get_desc()
    price = inventory[int(selection)-1].get_price()
    unitCount = inventory[int(selection)-1].get_unitCount()
    item.set_desc(desc)
    item.set_price(price)
    purchase_count = input('How many would you like to purchase?\n')
    while purchase_count.isnumeric == False or int(purchase_count) > int(unitCount) :
        purchase_count = input('We do not have that many in stock. How many would you like to purchase?\n')
    item.set_unitCount(purchase_count)
    inventory[int(selection)-1].set_unitCount(int(unitCount) - int(purchase_count))
    register.purchase_item(item)

def readData(filename):
    # Opening the file in read mode
    data = open(filename, 'rb')
    # Setting EOF to false
    end_of_file = False
    #Setting while loop to get each object in binary file
    while not end_of_file:
        try:
            #unpickle next object
            output = pickle.load(data)
            return output
        except EOFError:
            #Set flag to indicate EOF reached
            end_of_file = True
    emp_file.close()

main()
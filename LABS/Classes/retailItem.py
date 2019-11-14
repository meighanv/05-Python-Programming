""" 5. RetailItem Class
Write a class named RetailItem that holds data about an item in a retail store. The class
should store the following data in attributes: item description, units in inventory, and price.
Once you have written the class, write a program that creates three RetailItem objects
and stores the following data in them:
​
            Description     Units in Inventory  Price
Item #1     Jacket          12                  59.95
Item #2     Designer Jeans  40                  34.95
Item #3     Shirt           20                  24.95 """

class RetailItem:
    # defining default attributes
    def __init__(self):
        self.__desc = ''
        self.__unitCount = 0
        self.__price = 0.0

    # Define setters
    def set_desc(self, desc):
        self.__desc = desc

    def set_unitCount(self, unitCount):
        self.__unitCount = unitCount

    def set_price(self, price):
        self.__price = price

    # Define getters
    def get_desc(self):
        return self.__desc

    def get_unitCount(self):
        return self.__unitCount
    
    def get_price(self):
        return self.__price

""" # Define main
def main():
    # Initialize object storage list
    inventory = []

    # Iterate for input of data for 3 retail items
    for i in range(3):
        item = RetailItem()
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

main() """
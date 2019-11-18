""" 
7. Cash Register
    This exercise assumes that you have created the RetailItem class for Programming
    Exercise 5. Create a CashRegister class that can be used with the RetailItem class. The
    CashRegister class should be able to internally keep a list of RetailItem objects. The
    class should have the following methods:
        • A method named purchase_item that accepts a RetailItem object as an argument.
        Each time the purchase_item method is called, the RetailItem object that is passed as
        an argument should be added to the list.
        • A method named get_total that returns the total price of all the RetailItem objects
        stored in the CashRegister object’s internal list.
        • A method named show_items that displays data about the RetailItem objects stored
        in the CashRegister object’s internal list.
        • A method named clear that should clear the CashRegister object’s internal list.
    Demonstrate the CashRegister class in a program that allows the user to select several
    items for purchase. When the user is ready to check out, the program should display a list
    of all the items he or she has selected for purchase, as well as the total price.
 """
from functools import reduce
class CashRegister:

    def __init__ (self):
        self.__purchase = []
        self.__total = 0.0

    def set_total(self):
        # This code below was replaced by the uncommented lambda function
        # total = 0
        # for i in self.__purchase:
        #     total += float(i.get_price()) * float(i.get_unitCount())
        receipt = (item.get_price()*item.get_unitCount() for item in self.__purchase)
        self.__total = reduce((lambda x,y: x + y), receipt)

    def purchase_item(self,item):
        self.__purchase.append(item)

    def get_total(self):
        return self.__total
    
    def show_items(self):
        for i in self.__purchase:
            print(i.get_desc())

    def clear_register(self):
        self.__purchase = []
        self.__total = 0.0
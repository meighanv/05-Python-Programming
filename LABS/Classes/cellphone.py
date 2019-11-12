"""
Wireless Solutions, Inc. is a business that sells cell phones and wireless service. 
You are a programmer in the company’s IT department, and your team is designing a program to manage
all of the cell phones that are in inventory. You have been asked to design a class that represents 
a cell phone. The data that should be kept as attributes in the class are as follows:
​
    • The name of the phone’s manufacturer will be assigned to the __manufact attribute.
    • The phone’s model number will be assigned to the __model attribute.
    • The phone’s retail price will be assigned to the __retail_price attribute.
​
The class will also have the following methods:
    • An __init__ method that accepts arguments for the manufacturer, model number,
    and retail price.
    • A set_manufact method that accepts an argument for the manufacturer. This
    method will allow us to change the value of the __manufact attribute after the object has been created, if necessary.
    • A set_model method that accepts an argument for the model. This method will allow
    us to change the value of the __model attribute after the object has been created, if
    necessary.
    • A set_retail_price method that accepts an argument for the retail price. This
    method will allow us to change the value of the __retail_price attribute after the
    object has been created, if necessary.
    • A get_manufact method that returns the phone’s manufacturer.
    • A get_model method that returns the phone’s model number.
    • A get_retail_price method that returns the phone’s retail price.
"""

# The CellPhone class pulls data about the cell phone

class CellPhone:
    # The __init__ method initializes the attributes
    def __init__(self,manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    #The set_manufact method accepts an argument for the phone's manufacturer
    def set_manufact(self, manufact):
        self.__manufact = manufact

    # The set_model method accepts an argument for the phone's model number
    def set_model(self, model):
        self.__model = model

    # The set_retail_price method accepts and arguement for retail price
    def set_retail_price(self, price):
        self.__retail_price = price 

    # The get_manufact method returns the phones manufacturer
    def get_manufact(self):
        return self.__manufact

    # The get_model method returns the phones model number
    def get_model(self):
        return self.__model

    # The get_price method returns the phones price
    def get_retail_price(self):
        return self.__retail_price
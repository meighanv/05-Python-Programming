class Person:
    def __init__(self, name, title, number):
        self.__name = name
        self.__title = title
        self.__number = number

    # Settors
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address
        
    def set_number(self, number):
        self.__number = number

    # Getters
    def get_name(self):
        self.__name

    def get_address(self):
        self.__address
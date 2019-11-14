class person:
    def __init__(self, name, address, number):
        self.__name = name
        self.__address = address
        self.__number = number

    # Settors
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address
        
    def set_number(self, number):
        self.__number = number

    # Getters
    def get_name(self, name):
        self.__name

    def get_address(self, address):
        self.__address
        
    def get_number(self, number):
        self.__number


class customer(person):
    def __init__(self, name, address, number, opt_in):
        super().__init__(name, number)

        self.__opt_in = opt_in
    
    def set_opt_in(self, opt_in):
        self.__opt_in = opt_in

    def get_opt_in(self):
        return self.__opt_in 

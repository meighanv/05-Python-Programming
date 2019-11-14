# The Automobile class holds general 
# data about and automobile object

class Automobile:
    # The __init__ method accepts arguments for
    #  the make, model, mileage, and price. It 
    # Initializes the data attributes with 
    # these values.

    # Set initial values for object
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Setting Settors
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model
    
    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # Setting Gettors
    def get_make(self):
        return self.__make 

    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price
        
# The car class represents a car. It is a subclass of the 
# automobile class
class Car(Automobile):
    
    # The init method accepts args for the car's make model mileage price and doors
    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's __init__ method and pass 
        # the required args. Note that we also have to 
        # pass self as an arg
        super().__init__(make, model, mileage, price)

        # Init the __doors
        self.__doors = doors

    # The set_doors method is the mutator for the __doors attribute
    def set_doors(self, doors):
        self.__doors = doors

    # Gettor for doors
    def get_doors(self):
        return self.__doors

# The ctruck class represents a truck. It is a subclass of the 
# automobile class
class Trucks(Automobile):
    
    # The init method accepts args for the truck's make model
    # mileage price and drive type
    def __init__(self, make, model, mileage, price, drive_type):
        # Call the superclass's __init__ method and pass 
        # the required args. 
        super().__init__(make, model, mileage, price)

        # Init the __drive_type attribute
        self.__drive_type = drive_type

    # The set_doors method is the mutator for the __doors attribute
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    # Gettor for doors
    def get_drive_type(self):
        return self.__drive_type

# The SUV class represents a truck. It is a subclass of the 
# automobile class
class SUV(Automobile):
    
    # The init method accepts args for the SUV's make model
    # mileage price and drive type
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass's __init__ method and pass 
        # the required args. 
        super().__init__(make, model, mileage, price)

        # Init the __pass_cap attribute
        self.__pass_cap = pass_cap

    # The set_doors method is the mutator for the __doors attribute
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # Gettor for doors
    def get_pass_cap(self):
        return self.__pass_cap
class Employee:
    # Initializing Mammal object attributes
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    # Initializing ProductionWorker subclass object attributes
    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)

        self.__shift = shift
        self.__pay_rate = pay_rate
    
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate    
    
    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate


class ShiftSupervisor(Employee):
    # Initializing ProductionWorker subclass object attributes
    def __init__(self, name, number, salary, prod_bonus):
        super().__init__(name, number)

        self.__salary = salary
        self.__prod_bonus = prod_bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_prod_bonus(self, prod_bonus):
        self.__prod_bonus = prod_bonus    
    
    def get_salary(self):
        return self.__salary

    def get_prod_bonus(self):
        return self.__prod_bonus
    


class Car:
    def __init__(self):
        self.__year_model = ''
        self.__make = ''
        self.__speed = 0
    
    def set_year_model(self):    
        self.__year_model = input('What is the year and model of your car? (i.e. 2015 Camaro)\n')
    
    def set_make(self):
        self.__make = input('What is the make of your car?\n')
    
    def set_age(self):
        self.__speed = input('What is the current speed? (In MPH)\n')
    
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make
    


""" def main ():
    my_car = Car()
    my_car.set_year_model()
    my_car.set_make()
    
    for i in range(5):
        my_car.accelerate()
        print(f'You are now traveling at {str(my_car.get_speed())} MPH in your {str(my_car.get_year_model())}.')


    

main() """
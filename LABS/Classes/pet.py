class Pet:
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = 0
    
    def set_name(self):    
        self.__name = input('What is the name of your pet?\n')
    
    def set_animal_type(self):
        self.__animal_type = input('What type of animal is your pet?\n')
    
    def set_age(self):
        self.__age = input('What is the age of your pet? (In human years)\n')
    
    def get_name(self):
        #print(f'Your pet\'s name is {self.__name}')
        return self.__name

    def get_type(self):
        #print(f'Your pet\'s is of the {self.__animal_type} species')
        return self.__animal_type

    def get_age(self):
        #print(f'Your pet\'s is {str(self.__age)} years old.')
        return self.__age



""" def main ():
    my_pet = Pet()
    my_pet.set_name()
    my_pet.set_animal_type()
    my_pet.set_age()

    print('Your Pet\'s Bio:')
    print(my_pet.get_name())
    print(my_pet.get_type())
    print(my_pet.get_age())

main() """
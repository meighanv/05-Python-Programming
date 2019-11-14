class Mammal:
    # Initializing Mammal object attributes
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a ', self.__species)

    def make_sound(self):
        print('Grrr')


class Dog(Mammal):
    # Initializing Dog subclass object attributes
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # This is an overide because it has the same name 
    # as above, but this one will overwrite the 'Grrr'
    # sound
    def make_sound(self):
        print('Woof')


class Cat(Mammal):
    # Initializing Dog subclass object attributes
    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # This is an overide because it has the same name 
    # as above, but this one will overwrite the 'Grrr'
    # sound
    def make_sound(self):
        print('Meow')

# Define Main

def main():
    cat = Cat()
    cat.make_sound()
    cat.show_species()

    dog = Dog()
    dog.make_sound()
    dog.show_species()

    mammal = Mammal('fish')
    mammal.make_sound()
    mammal.show_species()

main()
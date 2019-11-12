# This is a class to create a super hero
class SuperHero:

    # This __init__ accepts an argument to set the hero's name
    def __init__(self, name):
        self.__name = name

    # This accepts an argument to set the hero's real name
    def set_real_name(self, realName):
        self.__real_name = realName

    # This accepts an argument to set the hero's powers
    def set_powers(self):
        self.__powers = []
        power = ''
        while power.upper() != 'DONE':
            power = input('What are your hero\'s powers? (Enter one at a time. Type \'DONE\' when finished)')
            if power.upper() != 'DONE':
                self.__powers.append(power)
    
    # This accepts an argument to set the hero's colors
    def set_colors(self):
        self.__colors = []
        color = ''
        while color.upper() != 'DONE':
            color = input('What colors does your hero wear? (Enter one at a time. Type \'DONE\' when finished)')
            if color.upper() != 'DONE':
                self.__powers.append(color)

    def get_name(self):
        print('Hero name: ', str(self.__name))
        print()
    
    def get_real_name(self):
        print('Hero\'s real name: ', str(self.__real_name))
        print()

    def get_powers(self):
        print('Hero\'s powers: ')
        for i in self.__powers:
            print(i)
        print()

    def get_colors(self):
        print('Hero\'s colors: ')
        for i in self.__colors:
            print(i)
        print()

def main():
    hero1 = SuperHero('Wolverine')
    hero1.set_real_name('Logan')
    hero1.set_powers()
    hero1.set_colors()

    hero1.get_name()
    hero1.get_real_name()
    hero1.get_powers()
    hero1.get_colors()


main()
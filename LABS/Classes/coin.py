#Classes

#A class is code that specifies the data attributes and methods for a particular type of object
import random
#The coin Coin class simulates a coin that can be flipped

class Coin:
    #the __init__ method is present in every class and initializes the sideup data attribute with heads
    def __init__(self):
        self.__sideup = 'Heads'

    # The toss method generateds a random number
    # in the range 0-1. If the number
    # is 0, then sideup is set to heads, 
    # otherwise, sideup is set to tails
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup
    def get_sideup(self):
        return self.__sideup 

# main function to operate with this class
def main():
    #Create an object from the coin class
    my_coin = Coin()
    type(my_coin)

    # sideup attribute is not private
    my_coin.__sideup = 'Tails'
    #If we don't want the user to set that variable 
    # it needs to be private. Prepend the variable with __
    # It will not error, but it prevents the assignment

    #Display the side of the coin that is facing up
    print('This side is up: ', my_coin.get_sideup())

    #Toss the coin
    print('I am tossing the coin ....')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())


    #Display the side of the coin that is facing up
    print('This side is up: ', my_coin.get_sideup())


#main()
####
#More Lecture notes
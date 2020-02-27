# This program imports the coin module and
# creates an instance of the Coin class

import coin

def main():
    #Create an object from the Coin class
    my_coin = coin.Coin()

    #display the side of the coin that is facing up
    print('This side is up: ', my_coin.get_sideup())

    #Toss the coin
    print('I am tossing the coin ten times ....')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

#Call Main
main()
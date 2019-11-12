# This program imports the simulation module and
# creates three instances of the Coin class

import coin

def main ():
    #Create three coins from the Coin class
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    #Show the state of the coins
    print('I have three coins with these sides up:')
    print('Coin 1: ', coin1.get_sideup())
    print('Coin 2: ', coin2.get_sideup())
    print('Coin 3: ', coin3.get_sideup())

    #Toss the coins
    print('I am tossing the coins...')
    print()
    coin1.toss()
    coin1.toss()
    coin1.toss()

    #Show the state of the coins
    print('I have three coins with these sides up:')
    print('Coin 1: ', coin1.get_sideup())
    print('Coin 2: ', coin2.get_sideup())
    print('Coin 3: ', coin3.get_sideup())

main()
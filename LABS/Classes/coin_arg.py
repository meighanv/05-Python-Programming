# This program passes a Coin object as
# an argument to a function
import coin

#main function
def main():
    # create a coin object
    my_coin = coin.Coin()

    # This might display 'Heads' or 'Tails'
    print(my_coin.get_sideup())
    
    # This will display 'Heads'
    flip(my_coin)

    # This might display 'Heads' or 'Tails'
    print(my_coin.get_sideup())

def flip(coin_obj):
    coin_obj.toss()

main()
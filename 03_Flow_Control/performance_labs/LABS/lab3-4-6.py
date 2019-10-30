#Defining constant values for coin currency
CURRENCY = {'DOLLAR': 1.00,
    'QUARTER': 0.25,
    'DIME': 0.10,
    'NICKEL': 0.05,
    'PENNY': 0.01,
    }

def main():
    #Get the total currency
    total = getCurrency()

    #Determine if total matches the value of a dollar
    matchDollar(total)

#Prompt user for coin input
def getCurrency():
    #initalizing 'total' variable
    total = float(0.00)

    #Loop through the global dictionary for currency
    for i in CURRENCY:
        #Skipping 'DOLLAR' because it is currency but not typically a coin
        if i != 'DOLLAR':
            #Setting denomination to the key
            denom = i
            #Setting value to the key value in the dictonary
            value = CURRENCY[i]
            #Getting amount of coin input from user; could utilize some input validation
            coins = int(input('Provide the number of {} coins you have:\n'.format(denom.lower())))
            #Calculate the monatary value of this group of coins
            coinsVal = float(coins) * float(value)
            #Adding the value of the coins to the running total
            total += coinsVal
    #returning the running total to main
    return total

#Compare the running total to the value of a dollar
def matchDollar(total):
    if total == CURRENCY['DOLLAR']:
        print('Congratulations! You have an exact dollar')
    elif total > CURRENCY['DOLLAR']:
        print('You do not have an exact dollar. You have more.')
    else:
        print('You do not have an exact dollar. You have less.')

main()

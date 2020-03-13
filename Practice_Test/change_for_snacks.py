'''
Write the function computeChange that receives a dictionary with the following possible keys:

'H' - half dollar
'Q' - quarter
'D' - dime
'N' - nickel
'P' - penny

Each key will have an associated integer value representing a quantity. The dictionary will represent a gathering
of change (coins). Your function will compute the total amount of change and determine whether or not there is
enough money to purchase items at a fast-food restaurant. If you have $2.50 or more you can buy BOTH fries
and a soda.  If you have at least $1.50 but less than $2.50 can buy FRIES. If you have at least $1.00 but less than $1.50
you can get a SODA. If you have less than $1.00 you get NOTHING.

For example, you may receive a dictionary such as {'Q':3, 'D':7, 'P':14} which would compute to $1.59. (3 quarters,
7 dimes, 14 pennies)

If any quantity in the dictionary is less than zero, the function will return a single value of zero (0), otherwise
the function should return two values: 
                                       1. Total money in the form of a Float (dollar representation with two decimal places)  
									         e.g. 1.59
                                       2. A string representing what could be purchased (if anything). Use
                                       one of the following strings:
                                            'NOTHING'
                                            'SODA'
                                            'FRIES'
                                            'BOTH'

return the total money as the first value, followed by the string representing the purchase as the second value


'''


def computeChange(change):
    # Setting values for each possible currency denomination
    values = {'H':0.5, 'Q':0.25, 'D':0.10, 'N':0.05, 'P':0.01}
    
    #setting accumulator
    total = 0.00

    #Iterating through each of the keys in the change dictionary
    for denom in change.keys():
        if change[denom] < 0:
            return 0
        else:
            total += change[denom] * values[denom]
    # Checking the total to return the possible purchased items
    if total < 1:
        # All returns require that total is rounded to two decimal places because
        # floating point math is slightly inaccurate in the way they are stored.
        return round(total,2), f'NOTHING'
    elif total < 1.5:
        return round(total,2), f'SODA'
    elif total < 2.5:
        return round(total,2), f'FRIES'
    else:
        return round(total,2), f'BOTH' 

    return 0, ''

print(computeChange({'Q':3, 'D':7, 'P':14}))

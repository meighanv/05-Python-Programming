#Set Roman numeral array
NUMERALS = ["I","II","III","IV","V","VI","VII","VIII","IX","X"]

def main():
    selection = getNumber()
    print('Your number in roman numerals is {}'.format(getNumeral(selection)))


def getNumeral(num):
    return NUMERALS[num-1]

def getNumber():
    select = 0 
    while int(select) > 10 or int(select) < 1:
        select = input('Please provide a number between 1 and 10:\n')
        if int(select) > 10:
            print('Number too high!')
        elif int(select) < 1:
            print('Number too low!')
    return int(select)

main()
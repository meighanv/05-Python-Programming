#Set Roman numeral array
NUMERALS = ["I","II","III","IV","V","VI","VII","VIII","IX","X"]

def main():
    #Store user input for the number they want to convert
    selection = getNumber()
    #Displays the number based on user input and it's reference to the dict
    print('Your number in roman numerals is {}'.format(getNumeral(selection)))

#Takes the number they input and subtracts 1 to fix 'off by one'
def getNumeral(num):
    return NUMERALS[num-1]

#Function with input validation to ensure it is in range
def getNumber():
    #Initializes selection
    select = 0 
    #Ensures number provided is between 1 and 10
    while int(select) > 10 or int(select) < 1:
        select = input('Please provide a number between 1 and 10:\n')
        #determines which side of the range they are on for an adjustment
        if int(select) > 10:
            print('Number too high!')
        elif int(select) < 1:
            print('Number too low!')
    #returns the selection to main
    return int(select)

main()
#Setting up main function
def main():
    #Calling Discount function passing result of the numPurchase function as an argument
    calcDiscount(int(numPurchase()))

#Defining function to capture and validate the user's input of the number of packages purchased
def numPurchase():
    #Getting initial input
    packages = input('How many packages did you buy:\n')
    #Validating input to be numeric and greater than 0
    while int(packages) < 0 or packages.isnumeric() == False:
        packages = input('Invalid input. How many packages did you buy:\n')
    #Returning result to main
    return packages

#Function to determine the level of discount
def calcDiscount(num):
    #No discount if less than 10 packages purchased
    if num < 10:
        print('There is no discount for {} purchases'.format(num))
    #20 percent discount 10-19 packages purchased
    elif num >= 10 and num <= 19:
        print('There is a 20 percent discount for {} purchases'.format(num))
    #30 percent discount 20-49 packages purchased
    elif num >= 20 and num <= 49:
        print('There is a 30 percent discount for {} purchases'.format(num))
    #40 percent discount 50-99 packages purchased
    elif num >= 50 and num <= 99:
        print('There is a 40 percent discount for {} purchases'.format(num))
    elif num >= 100:
        print('There is a 50 percent discount for {} purchases'.format(num))

main()
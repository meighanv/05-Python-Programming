#Setting up main function
def main():
    #Calling Charge function passing result of the getWeight function as an argument
    calcCharge(float(getWeight()))

#Defining function to capture and validate the user's input of the number of packages purchased
def getWeight():
    #Getting initial input
    packageWeight = input('What is the weight of your package:\n')
    #Validating input to be numeric and greater than 0.00
    while float(packageWeight) < 0 or packageWeight.replace('.','').isnumeric() == False:
        packageWeight = input('Invalid input. What is the weight of your package:\n')
    #Returning result to main
    return packageWeight

#Function to determine shipping charge
def calcCharge(num):
    #Charge for less than 2 pounds
    if num <= 2.00:
        print('The shipping charge is $1.10')
    #Charge for over 2 pounds upt0 6
    elif num > 2 and num <= 6:
        print('The shipping charge is $2.20')
    #Charge for over 6 pounds upto 10
    elif num > 6 and num <= 10:
        print('The shipping charge is $3.70')
    #Charge for more than 10 pounds
    elif num > 10:
        print('The shipping charge is $3.80')
    

main()
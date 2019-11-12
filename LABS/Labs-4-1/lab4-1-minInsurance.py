#Miminum percentage of replacement cost
FLOOR_PERC = 0.80

#Define the main function
def main():
    calcMin(getCost())

#User input for the replacement building cost with input validation to be returned to main    
def getCost():
    #Initial prompt for input
    cost = input('What is the replacement cost of your building?\n')
    #Input validation checking numeric and a positive number
    while float(cost) <= 0 and cost.replace('.','').isnumeric() == False:
        cost = input('Invalid input. What is the replacement cost of your building?\n')
    return cost

#Function to print the minimum insurance based on replacement cost in a statement
def calcMin(cost):
    print('Your building must be insured for ${:.2f}'.format(float(cost)*FLOOR_PERC))

main()

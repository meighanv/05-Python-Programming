#Define Constant for number of months
NUM_MONTHS=12

#Main function
def main():
    category = ['loan payment','insurance','gas','oil','tires','maintenance']
    expenses = []
    getExpenses(category,expenses)
    displayCosts(category,expenses)
#Iterates through the expense items 
def getExpenses(category,expenses):
    for i in category:
        #Appends the cost of the category to 'expenses'
        # by passing i as an argument for getCost which then fills in the question
        expenses.append(getCost(i))

#Defining a function to take in a prompt as a question 
# and validate input as positive and numeric
def getCost(prompt):
    cost = input('Please enter the montly costs for {:s}:\n'.format(prompt))
    #Input validation checking numeric and a positive number
    while float(cost) <= 0 and cost.replace('.','').isnumeric() == False:
        cost = input('Invalid input. Please enter the montly costs for {:s}:\n'.format(prompt))
    return float(cost)

#Define function for displayCosts
def displayCosts(category, expenses):
    total = 0.0
    for i in range(len(category)):
        print('Expense for {:s}: ${:.2f}'.format(category[i],expenses[i]))
        total += float(expenses[i])
    print('-'*30)
    print('Monthly total expenses: ${:.2f}'.format(float(total)))
    print('Annual Total: ${:.2f}'.format(float(total)*NUM_MONTHS))

main()
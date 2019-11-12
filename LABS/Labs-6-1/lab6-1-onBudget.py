#Define main
def main():
    budget = getBudget()
    expenses = []
    getExpenses(expenses)
    overOrUnder(budget,totalExp(expenses))


def getBudget():
    budget = input('What is your budget? (Ex: 3206.10):\n')
    #Input validation checking numeric and a positive number
    while float(budget) <= 0 and budget.replace('.','').isnumeric() == False:
        budget = input('Invalid input. What is your budget? (Ex: 3206.10):\n')
    return float(budget)

def getExpenses(expenseList):
    done = False
    while done == False:
        expense = input('Input an expense (206.10). Type "exit" when no more expenses are to be entered:\n')
        try:
            #Input validation checking numeric and a positive number
            while float(expense) <= 0 and expense.replace('.','').isnumeric() == False:
                expense = input('Input an expense (206.10). Type "exit" when no more expenses are to be entered:\n')
            expenseList.append(float(expense))
        except:
            done = True 
            

def totalExp(expenseList):
    total = 0.0
    for i in expenseList:
        total += float(i)
    return total

def overOrUnder(cap,spent):
    if spent > cap:
        print('You are overbudget by ${:.2f}!'.format(spent-cap))
    elif cap > spent:
        print('You are ${:.2f} under budget!'.format(cap-spent))
    else:
        print('You are right on budget!')

main()
#Defining Variables for profit calculator
projProfit = 0.23

#Requesting user input for totalSales
totalSales = input('What is the profected total annual sales?')

#Calculate profit
profit = float(totalSales)*projProfit

#Printing profit result to screen with appropriate float formatting for money
print("Total projected profit is $%.2f" % profit)
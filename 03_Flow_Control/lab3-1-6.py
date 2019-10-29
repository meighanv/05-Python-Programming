#Setting variable for state and county tax
stateTax = 0.04
countyTax = 0.02

#User input for amount of purchase
purchase = input("Input amount of purchase: \n")
#Input validation for numeric
#Using .replace to get rid of decimal to validate input is numeric

while purchase.replace('.','').isnumeric() == False:
    purchase = input("Input was not valid. Input amount of purchase:\n")

print('State Tax: ${:.2f}'.format(float(purchase) * stateTax))
print('County Tax: ${:.2f}'.format(float(purchase) * countyTax))
print('Total Tax: ${:.2f}'.format((float(purchase) * stateTax) + (float(purchase) * countyTax) ))
print('State Tax: ${:.2f}'.format((float(purchase) * stateTax) + (float(purchase) * countyTax) + float(purchase)))

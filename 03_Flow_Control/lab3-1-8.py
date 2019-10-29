#Setting variable for tip and sales tax
salesTax = 0.07
tip = 0.15

#User input for amount of meal purchase
purchase = input("Input amount of meal purchase: \n")
#Input validation for numeric
#Using .replace to get rid of decimal to validate input is numeric
while purchase.replace('.','').isnumeric() == False:
    purchase = input("Input was not valid. Input amount of purchase:\n")

print('Sales Tax: ${:.2f}'.format(float(purchase) * salesTax))
print('Tip at 15%: ${:.2f}'.format(float(purchase) * tip))
print('State Tax: ${:.2f}'.format((float(purchase) * salesTax) + (float(purchase) * tip) + float(purchase)))

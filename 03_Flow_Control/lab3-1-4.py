## Subtotal of items purchased
#define initialized variable for total
total = 0
salesTax = 0.06

#Ask the user for the number of items
itemCount = input('How many items did you purchase?\n')

#Initialize item price list as input from user
items = [0] * int(itemCount)

#init while counter for loop through the number of items specified
count = 1

#Begin while loop starting from count to itemCount
while int(count) <= int(itemCount):
    item = input("Input price of item {} \n".format(count))
    #Input validation for numeric
    #Using .replace to get rid of decimal to validate input is numeric
    while item.replace('.','').isnumeric() == False:
        item = input("Input was not a number. Input price of item {}\n".format(count))
    #Add item price to items array
    items[count-1] = item
    #incrememnt counter
    count += 1

#loop through array to create subtotal
subtotal = 0.00
for i in items:
    subtotal += float(i)
    
print('Subtotal: ${:.2f}\n'.format(subtotal))
print('Sales Tax: ${:.2f}\n'.format(float(subtotal*salesTax)))
print('Total: ${:.2f}\n'.format(float(subtotal +(subtotal*salesTax))))
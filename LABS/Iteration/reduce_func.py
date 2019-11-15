# reduce()
# Receives two argsm function and iterable
# returns a single value
# good for rolling computation to sequential 
# pairs of values in a list

# Factorial is like factorial 3  is 3 * 2 * 1 = 6

import functools

# Define our function
def mult(x, y):
    print('x = ', x, 'y = ', y)
    return x*y

# Apply reduce to our function
fact = functools.reduce(mult, range(1,4))
print('Factorial of 3 is ', fact)

product = 1
mylist = [1, 2, 3, 4, ]
""" for num in mylist:
    product = product * num """

from functools import reduce
product = reduce((lambda x, y: x*y), mylist)
print(product)
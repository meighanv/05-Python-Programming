"""
4. 
    (The sqrt function) Write a program that prints the following table
    using your knowledge of loops and the sqrt function in the math module.
    Make sure your table is neat by using print formatting methods we've learned. 
​
        Number  Square Root
        0       0.0000
        1       1.0000
        2       1.4142
        ...
        18      4.2426
        20      4.4721
    # could use list comprehension and lambda for this after importing math sqrt
"""
# This program is mean to perform the prompt above

# Importing the sqrt() function from math
from math import sqrt
def main():
    # Printing table header
    print('Number\tSquare Root')
    # Looping through numbers 0-20
    for i in range(21):
        # Printing the number with a \t for spacing readability and 
        # the actual sqrt result
        print(f'{i}\t{sqrt(i)}')

main()
        
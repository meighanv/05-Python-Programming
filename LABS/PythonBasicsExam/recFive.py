""" 
Have a user input a list of at least 5 integers. Write a function to find the 
GCD (greatest common divisor) of two randomly selected numbers from the list by 
using recursion. Output the answer to the terminal.
​
The greatest common divisor of two or more integers, which are not all zero, is 
the largest positive integer that divides each of the integers. For example, the 
gcd of 8 and 12 is 4.
"""
import random

def get_intList():
    userlist = []
    while len(userlist) < 5:
        userInput = input('Provide an integer: ')
        try:
            int(userInput)
            userlist.append(int(userInput))
        except ValueError:
            print('Input Error. Provide an integer: ')
        
    return userlist

def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a%b)

def main():
    userlist = get_intList()
    randa = random.randint(0, len(userlist))
    randb = random.randint(0, len(userlist))
    while randa == randb:
        randb = userlist[random.randint(0, len(userlist))]
    a = userlist[randa]
    b = userlist[randb]
    
    print(f'The GCD of {a} and {b} is: {get_gcd(a,b)}')

main()
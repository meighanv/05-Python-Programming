""" 6. Sum of Numbers
    Design a function that accepts an integer argument and returns the sum of all the integers from 1 up 
    to the number passed as an argument. For example, if 50 is passed as an argument, the function will 
    return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum. """

def main():
    print(getSumTerm(5))

def getSumTerm(x):
    if x == -1:
        return 0
    else:
        return getSumTerm(x-1) + x
main()
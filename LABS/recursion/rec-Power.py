""" 7. Recursive Power Method
    Design a function that uses recursion to raise a number to a power. The function should
    accept two arguments: the number to be raised and the exponent. Assume that the exponent is a 
    nonnegative integer. """

def main():
    print(getPower(7,2))

def getPower(x,y):
    if x == 0:
        return 1
    else:
        return getPower(x-1,y) * y
        
main()
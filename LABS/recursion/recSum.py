""" 5. Recursive List Sum
    Design a function that accepts a list of numbers as an argument. The function should recursively 
    calculate the sum of all the numbers in the list and return that value. """

def main():
    myList = [1000,6,1,9,20,30,29,3]
    print(getSum(myList,len(myList)-1))

def getSum(array,x):
    if x == -1:
        return 0
    else:
        return getSum(array,x-1) + array[x]
main()
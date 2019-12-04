"""
1. The list method reverse reverses the elements in the list. Define a function named reverse that 
reverses the elements in its list argument (without using the method reverse). Try to make this 
function as efficient as possible, and state its computational complexity using big-O notation. 
​
2. Python’s pow function returns the result of raising a number to a given power. Define a function 
expo that performs this task and state its computational com-plexity using big-O notation. The first 
argument of this function is the number, and the second argument is the exponent (nonnegative numbers only). 
You can use either a loop or a recursive function in your implementation, but do not use Python’s ** operator 
or pow function. 
"""
# # Swap function used to exchange positions of two elements
# def swap(myList, i , j):
#     # Exchanges the positions of two items in a list
#     temp = myList[i]
#     myList[i] = myList[j]
#     myList[j] = temp

# # Reverse function, attacks the list from both ends swapping elements 
# # until the start/end boundaries pass each other
# def reverse(myList):
#     # Boundary - first element
#     start = 0
#     # Boundary - last element
#     end = len(myList) - 1
#     while start < end:
#         swap(myList, start, end)
#         # Move the boundaries closer to the middle
#         start += 1
#         end -= 1

# # Big O = O(n)
# import random

# myList = []
# for i in range(10):
#     myList.append(random.randint(0,100))

# print(myList)
# reverse(myList)
# print(myList)


# This next function will satisfy prompt 2
def expo(base, exponent):
    # setting product (accumulator) to base for base number
    product = base
    if exponent == 0:
        return 1
    else:
        # looping exponent # of times (subtracting 1 for since base was already started)
        for i in range(exponent-1):
            product *= base
        return product

def main():
    print(expo(2, 5))

main()

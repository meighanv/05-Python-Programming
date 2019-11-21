# # This is an example of recursion, where the function (annoying) calls itself until python kills it
# def forever(times):
#     annoying(times)

# def annoying(times):
#     if times > 0:
#         print('Test message')
#         annoying(times - 1)

# def main():
#     forever(500)

# main()

# # Must have something to kill your recursion
# # Depth of recursion is the number of times it calls itself
# def recursive_factorial(n):
#     # Start with base case (If the problem can be solved now,
#     #  then the function solves it and returns)
#     if n == 0:
#         return 1
#     #Recursive case (If the problem cannot be solved now, 
#     # then the function reduces it to smaller similar problems
#     # and calls itself to solve the smaller problem)
#     else:
#         return n * recursive_factorial(n-1)

# print(recursive_factorial(4))


# Range sum function
# def main():
#     # Create a list of numbers 
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#     # Get the sim of the items at indicies 2 - 5
#     my_sum = range_sum(numbers, 2, 5)

#     # Display the sum
#     print('The sum of items 2 - 5 is ', my_sum)

# The range_sum function returns the sum of a specified 
# range of items in the num_list. The start parameter
# specified the index of the starting item. The end 
# parameter specifies the index of the ending item
# def range_sum(num_list, start, end):
#     #base case
#     if start > end:
#         return 0
#     # recursive case
#     else:
#         return num_list[start] + range_sum(num_list, start + 1, end) 

# main()

# Fibonacci returns the nth number in the fibonacci series
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# for i in range(0,50):
#     print(fibonacci(i))


# GCD greatest common divisor(denominator)

# if x can evenly be divided by y then gcd(x, y) = y
# Otherwise, gcd(x,y) = gcd(y, remainder of x/y)

# def main():
#     # Get two numbers
#     num1 = int(input('Enter an integer: \n'))
#     num2 = int(input('Enter another integer: \n'))

#     # Display the GCD
#     print('The greatest common divisor of\nthe two numbers is: ', gcd(num1,num2))

# def gcd(x,y):
#     #base case
#     if x % y == 0:
#         return y
#     else:
#         return gcd(y, x % y)
        
# # The GCD returns the greates common divisor of two numbers
# main()

## Towers of Hanoi
# RULES
    # Only one disc may be moved at a time
    # A disc cannot be placed on top of another 
    # disk
    # All discs must be stored on a peg while it's being moved 
    # You must move all discs from the third peg to the first peg 

# This program simulates the Towers of Hanoi Game
def main():
    # set up some initial values
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    moveDiscs(num_discs, from_peg, to_peg, temp_peg)
    print('All the discs are moved')


# The moveDiscs function displays a disc move in
# the Towers of Hanoi game
# The parameters are:
#   num:        the number of discs to move
#   from_peg:   the peg to move from 
#   to_peg:     the peg to move to
#   temp_peg    the temporary peg
def moveDiscs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        moveDiscs(num -1, from_peg, temp_peg, to_peg)
        print('Move a disc from peg', from_peg, 'to_peg ', to_peg)
        moveDiscs(num -1, temp_peg, to_peg, from_peg) 

# Call main
main()
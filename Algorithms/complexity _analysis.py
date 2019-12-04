# *****************COMPLEXITY ANALYSIS*****************
# Complexity analysis - a method of determining the efficiency of 
#                       algorithms that allows you to rate them 
#                       independently of platform-dependent timings 
#                       or impractical instructional counts

# Order of complexity - the difference in performance of your algorithms



# linear - 'n' = our problem size (directly proportional growth) 
# quadratic - n^2 = a nested loop of our problem size (grows as a function 
#             of the square of the problem size)
# logarithmic - proportional to log base 2 of the problem size log 2 n = is 
#               more efficient than n^2 or 2^n
#     A logrithm is the power to which a number must be raised to be equal 
#     to another number (recursion)

# polynomial time algorithm - grows at a rate of n raised to the k (in same 
#                             category as quadratic as far as order)

# exponential - (worst performance) grows at a rate of 2^n

# *****************Big-O Notation*****************
# dominant - the amount of work in an algorithm that becomes so large that 
# you can ignore the amount of work represented by the other terms
#     (1/2)n^2-(1/2)n 
#     n^2 is the dominant term
#     (1/2) - a constant of proportionality

#     Represented in Big-O:
#     O(n^2)

# Constant O(1)
#     - Time taken is independent of the amount of data
#     - Stack push, pop and peek; Queue, dequeue and enqueue; insert a node 
#     into a linked list

# Linear O(n)
#     - Time take is directly proportional to the amount of data
#     - Linear search; Count items in a list; compare a pair of strings

# Quadratic O(n^2)
#     - Time taken is proportional to the amount of data squared; twice as 
#     much data takes 4x time to process; 3x takes 9x
#     - Bubble sort; selection sort; insertion sort; Traverse a 2D array

# Polynomial O(n^k)
#     - Time taken is proportional to the amount of data raised to the power
#     of a constant 
#     - 

# Logorithmic O(log n)
#     - Time taken is proportional to the logarithm of the amount of data,
#      good scalability
#     -Binary search a sorted list; Search a binary tree; Divide and Conquer
#      algorithm approaches

# Linearithmic O(n log n)
#     - Time taken is proportional to the logarithm of the amount of data, 
#     multiplied by the amount of data 

# Exponential O(k^n)
#     - Time taken is proportional to a constant raised to the power of the
#      amount of data, very poor scalability almost immediately
#     - If constant k is 10, then one extra item of data will slow it down
#      by 10 times 

# Logarithms - The inverse of exponentiation
#     Generally - 
#         x^z = y         log base x of y = z
#         2^0 = 1         log base 2 of 1 = 0
#         2^1 = 2         log base 2 of 2 = 1
#         2^2 = 4         log base 2 of 4 = 2
#         2^3 = 8         log base 2 of 8 = 3
#         2^4 = 16        log base 2 of 16 = 4
#         10^4 = 10000    log base 10 of 10000 = 4

#         notice that each # that we're calculating the log of is twice as 
#         much as the previous #, but each log is only 1 bigger than the previous value


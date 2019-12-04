""" 
Basic Sort Algorithms

    The algorithms examined here are easy to write but inefficien
    Each alg we discuss here will utilize a list of integers and the 
    swap function defined below 
"""
import timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def swap(myList, i , j):
    # Exchanges the positions of two items in a list
    temp = myList[i]
    myList[i] = myList[j]
    myList[j] = temp

# *************************Selection Sort*************************
# Each pass through the main loop selets a single item to be moved
# Searches the list for the position of the smallest item
# If that position is not the first position it swaps the items at those
# positions 
# Ih then finds the next smallest itm and swaps the item at the second 
# position

def selectionSort(myList):
    i = 0
    # Do n-1 searches for the smallest item 
    while i < len(myList) - 1:
        minIndex = i
        j = i + 1
        while j < len(myList):
            if myList[j] < myList[minIndex]:
                minIndex = j
            j += 1
        #Exchange if needed
        if minIndex != i:
            swap(myList, minIndex, i)
        i += 1

"""
Big O: O(n^2)
(1/2)n^2 - (1/2)n

Because data items are swapped only in the outer loop, this additional 
cost for selection sort is linear in the worst and average cases.
"""

##############################BUBBLE SORT##############################
"""
The strategy is to start at the beginning of the list and compare pairs
of data items as it moves down to the end. Each time the pairs are out
of order, the algorithm swaps them. The largest item will swap them.
The largest item will eventually"bubble out to the end of the list.
"""

def bubSort(myList):
    n = len(myList)
    # do n - 1 searches 
    while n > 1:
        i = 1
        #start each bubble
        while i < n:
            if myList[i] < myList[i-1]:
                #exchange if needed
                swap(myList, i , i-1)
            i += 1
        n -= 1

"""
(1/2)n^2 -(1/2)n

O(n^2)
"""

# Update bubble sort to linear best case check
# In best case list is already sorted; there are no swaps
# We can modify alg to be more efficient

def bubbleSort(myList):
    n = len(myList)
    # do n - 1 searches 
    while n > 1:
        swapped = False
        i = 1
        #start each bubble
        while i < n:
            if myList[i] < myList[i-1]:
                #exchange if needed
                swap(myList, i , i-1)
                swapped = True
            i += 1
        if not swapped: return 
        n -= 1


#sortedList = [i for i in range(10000)]
unsorted = [3,2,6,99,46,22,85,12,98]

# print(unsorted)
# bubbleSort(unsorted)
# print(unsorted)

# unsorted = [3,2,6,99,46,22,85,12,98]
# print(unsorted)
# bubSort(unsorted)
# print(unsorted)

# wrapped = wrapper(bubSort, sortedList)
# print(f'bubSort of sorted: {timeit.timeit(wrapped, number=1)}')
# wrapped = wrapper(bubSort, unsorted)
# print(f'bubSort of unsorted: {timeit.timeit(wrapped, number=1000)}')

# wrapped = wrapper(bubbleSort, sortedList)
# print(f'bubbleSort of sorted: {timeit.timeit(wrapped, number=1000)}')
# wrapped = wrapper(bubbleSort, unsorted)
# print(f'bubbleSort of unsorted: {timeit.timeit(wrapped, number=1000)}')

##############################INSERTION SORT###########################
# On the ith pass through the list, where i ranges from 1 to n-1, the ith
# item should be inserted into its propoer place in the list amoung the 
# first i items in the list. After the ith pass, the first i items should 
# be in sorted order. This process is analagous to the way in which many 
# people organize playing cards . That is, if you hold the first --1 cards
# in order, you can pick the ith cadrd and compare it to these cards until 
# its proper spot is found
# Insertion  sort consists of two loops. The outer loops traverse the 
# positions from 1 to n-1. For each position i in this loop, you save the
# item and start the inner loop at position i-1. For each position J in 
# this loop, you move the item to position j+1 until youfind the insertion
# point for the saved(ith) item.
# 

def insertionSort(myList):
    i = 1
    while i < len(myList):
        itemToInsert = myList[j]:
        j = i-1
        while j >= 0:
            if itemToInsert < myList[j]:
                myList[j+1] = myList[j]
                j -= 1
            else:
                break
        myList[j+1] = itemToInsert
        i += 1

insertionSort(unsorted)
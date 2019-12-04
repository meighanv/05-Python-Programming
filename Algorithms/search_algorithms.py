""" 
# Search Algorithms

# This function mimics python's min()
# Use this function to strudy the complexity of this Algorithm
# by returning the index of the minimum item 
# This Algorithm assumes that the list is not empty and that the 
# items are not in order.
# This Algorithm starts by treating the first position as that of 
# the minimum item. It then searches to the right for a smaller 
# number, and if found resets the position. When it reaches the 
# end of the list it returns the position of the minimum item.

"""
# def indexOfMin(myList):
#     minIndex = 0
#     currentIndex = 1
#     while currentIndex < len(myList):
#         if myList[currentIndex] < myList[minIndex]:
#             minIndex = currentIndex
#         currentIndex += 1
#     return minIndex

# theList = [2,6,5,1,3,4,9]
# print(indexOfMin(theList))

""" 
# ***********************Sequential search******************************

# This function returns the position of the target item if found, 
# or -1 otherwise
 """
# def seqSearch(target, myList):
#     position = 0
#     while position < len(myList):
#         if target == myList[position]:
#             return position
#         position += 1
#     return -1
# theList = [2,6,5,1,3,4,9]
# print(seqSearch(2, theList))
""" 
# *************************BINARY SEARCH**********************************
# Requires a sorted list to start
# Used to search an ordered list for a pariticular value
# Divide and Conquer approach
# Target is compared with the middle value, then half the list is discared
#  repeatedly until the target is found 
 """
def binSearch(target, sortedList):
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        midpoint = (left +right) // 2
        if target == sortedList[midpoint]:
            return midpoint
        elif target < sortedList[midpoint]:
            right =  midpoint -1
        else:
            left = midpoint + 1
    return -1

myList = [1,2,3,4,5,6,7,8,9]
print(binSearch(10, myList))

""" 
For a list of size n we perform the reduction n/2/2/2/2.... until we get to 1

Let k be the number of times we divide by 2 then we get n/2^k =1

n = 2^k     --->    k = log base 2 of n 
"""
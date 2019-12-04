"""
Faster Sorting

Up until now we've leared about sorting methods with a O(n^2) complexity. Even
w/ mods they are only marginally better.

Let's now discuss some algs w/ a complexity of O(log n) or )(n log n)
The secret here is that we use our divide and conquer strategy

Each Alg finds a way of breaking the list into smaller lists. Then these sublists 
are sorted recursively. The # of subdivisions is  log(n) and the amount of work 
needed to rearrange the data on each subdivision is n, thus making our complexity 
O(n log n)
"""
"""
**********************QUICK SORT**********************
- The strategy here is theat we start with a PIVOT. Pivot can be anywhere but lets 
just start by setting our pivot to the midpoint.

- Partition items in the list so that all items less than the pivot move left of 
the pivot and the rest move right. The final position of the pivot after the list 
is sorted could be at the end of the list or the beginning of the list.

- Divide and Conquer. Reapply the process recursively to the sublists formed by 
splitting the list at the pivot. one sublist consists of all the items to the 
left of the pivot(now all the smaller items), and the other sublist has all items 
to the right of the pivot (larger items)

- Process terminates each time it encounters a sublist with fewer than two items

"""


def quickSort(myList):
    quickSortHelper(myList, 0, len(myList)-1)
    

# recursive function to hide extra arguments for the endpoints of a subset
def quickSortHelper(myList, left, right):
    if left < right:
        pivotLocation = partition(myList, left, right)
        # REcursively calls helper for the left of partition
        quickSortHelper(myList, left, pivotLocation - 1)
        # REcursively calls helper for the left of partition
        quickSortHelper(myList, pivotLocation + 1, right)


def partition(myList, left, right):
    middle = (left + right)//2
    pivot = myList[middle]
    myList[middle] = myList[right]
    myList[right] = pivot
    #set boundary point to  first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if myList[index] < pivot:
            swap(myList, index, boundary)
            boundary +=1
    swap(myList, right, boundary)
    return boundary

def swap(myList, i , j):
    # Exchanges the positions of two items in a list
    temp = myList[i]
    myList[i] = myList[j]
    myList[j] = temp

import random
def main(size = 20, sort = quickSort):
    myList = []
    for count in range(size):
        myList.append(random.randint(1,size + 1))
    print(myList)
    sort(myList)
    print(myList)

main()

"""
********************MERGE SORT************************

- Divide and conquer strategy
- Computer the middle position of a list and recursively sort its 
left and right sublists. 
- Merge the two sorted sublists back into a single sorted list
- Stop the process when sublists can no longer be subdivided

"""

# This is the merge sort function
from array import array

def mergeSort(myList):
    # CopyBuff is a temporary space needed during the merge
    copyBuffer = array(len(myList))
    mergeSortHelper(myList, copyBuffer, 0, len(myList) - 1)


# myList is being sorted
# copyBuffer = temp space needed during merge
# low, high = bounds of sublist
# middle = midpoint of sublist
def mergeSortHelper(myList, copyBuffer, low, high):
    if low < high:
        middle = (low + high) //2
        mergeSortHelper(myList, copyBuffer, low, middle)
        mergeSortHelper(myList, copyBuffer, middle +1, high)
        merge(myList, copyBuffer, low, middle, high)

# Init i1 and i2 to first items in each sublist
# The merge function combines two sorted sublists into a larger sorted list
# The first sublist lies between the low and middle and the second between 
# middle +1 and high
# - set up index pointers to the first items in each sublist (low and
#  middle + 1)
# - Starting w/ the st item in each sublist, repeatedly compare items. 
#   Copy the smaller
#   item from its sublist to the copy buffer and advance to the next 
#   item in sublist
# - copy the portion of copybuffer between low and high back to the 
#   corresponding positions in myList  
def merge(myList, copyBuffer, low, middle, high):
    i1 = low
    i2 = middle +1
    for i in range(low, high +1):
        if i1 > middle:
            # First sublist
            copyBuffer[i] = myList[i2]
            i2 += 1
        elif i2 > high:
            # second sublist exhausted
            copyBuffer[i] = myList[i2]
        elif myList[i1] < myList[i2]:
            copyBuffer[i] = myList[i1]
            i1 += 1
        else:
            copyBuffer[i] = myList[i2]
            i2 += 1
    #Copy sorted items back into proper position in the list
    for i in range(low, high +1):
        myList[i] = copyBuffer[i]

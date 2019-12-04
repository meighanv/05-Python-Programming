import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# This is meant to find the values of 44 and 90 in a sorted list

def binSearch(target, sortedList):
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedList[midpoint]:
            return midpoint
        elif target < sortedList[midpoint]:
            right =  midpoint -1
        else:
            left = midpoint + 1
        # Trace values print statement
        #print(f'Left = {left}, Right = {right}, Midpoint = {midpoint}')
    return -1

# myList = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
# print(binSearch(44, myList))
# print(binSearch(90, myList))

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)//2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1 

myList = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
#print(binarySearch(myList, 0, len(myList)-1, 44))
#print(binarySearch(myList, 0, len(myList)-1, 90))
wrapped = wrapper(binSearch, 44, myList)
print(f'Non-Recursive search for 44: {timeit.timeit(wrapped, number=1000)}')
wrapped = wrapper(binSearch, 90, myList)
print(f'Non-Recursive search for 90: {timeit.timeit(wrapped, number=1000)}')

wrapped = wrapper(binarySearch, myList, 0, len(myList)-1, 44)
print(f'Recursive search for 44: {timeit.timeit(wrapped, number=1000)}')
wrapped = wrapper(binarySearch, myList, 0, len(myList)-1, 90)
print(f'Recursive search for 90: {timeit.timeit(wrapped, number=1000)}')

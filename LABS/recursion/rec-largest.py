"""4. Largest List Item
    Design a function that accepts a list as an argument, and returns the largest value in the list.
    The function should use recursion to find the largest item.
"""

def main():
    myList = [10,6,1,9,20,30,29,3]
    print(findLargest(myList,len(myList)-1))

def findLargest(array,x):
    if x == -1:
        return 0
    else:
        largest = findLargest(array,x-1)
        if array[x] > largest:
            largest = array[x]
        return largest
main()

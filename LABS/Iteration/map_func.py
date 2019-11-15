# map() function
# calls a specified function and applies it to each item of an iterable

def square(x):
    return x*x

numbers = [1, 2, 3, 4, 5]

# Uses the map function to square each item in the list of numbers
#sqrList = map(square, numbers)
#print(next(sqrList))
#print(next(sqrList))
#print(next(sqrList))
#print(next(sqrList))
#print(next(sqrList))
#print(next(sqrList))

""" sqrList2 = map(lambda x: x*x, numbers)
print(next(sqrList2))
print(next(sqrList2))
print(next(sqrList2))
print(next(sqrList2))
print(next(sqrList2))
print(next(sqrList2)) """

# Use of map is map(<function>, arg1, arg2)
tens = [10, 20, 30, 40, 50]
indx = [1, 2, 3, 4, 5]
powers = list(map(pow, tens, indx))
print(powers)


mydict= {}
dir(mydict)
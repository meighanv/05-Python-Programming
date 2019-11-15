myList = [1, 2, 3, 4]

l1 =  [1, 2, 3, 4]
it = iter(l1)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
# This will produce a 'StopIteration' error
print(it.__next__())

# An alternative to the statement above
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# If something is not iterable it will say 'object is not iterable'
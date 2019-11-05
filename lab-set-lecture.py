#Set contains a collection of unique values
#and works like a mathematical set

#All the elements in a set must be unique, no two elements can have the same value

#Sets are unordered

#Elements stored in a set can be of different data types
mySet= set(['a','b','c'])
print(mySet)

mySet2 = set('abc')
print(mySet2)

mySet3 = set('aabbcc')
print(mySet3)
#All of the above appear the same when printed

#set can only take on arg
#mySet4 = set('one','two','three') is invalid

mySet4 = set('one,two,three')
print(mySet4)

newSet = set()
newSet.add(1)
newSet.add(2)
newSet.add(3)
print('newSet', newSet)

newSet.update([4,5,6])

newSet2 = ([7,8,9])
newSet.update(newSet2)

newSet.remove(1)

#using for loop to iterate
newSet3 = set('abc')
for val in newSet3:
    print(val)

numbers_set([1, 2, 3])
if 1 in numbers_set:
    print('The value {} is in the set'.format(val))

if 99 not in numbers_set:
    print('The value {} is not in the set'.format(val))

#unions
set1= set([1,2,3,4])
set2= set([3,4,5,6])
set3= set1.union(set2)
print(set1)
print(set2)
print(set3)

set5= set1|set2

#Find intersection
set4= set1.intersection(set2)
print(set4)
set6= set1&set2

charSet = ('abc')
charSetUpper = ('ABC')

#difference 
set7 = set1.difference(set2)
set8 = set2.difference(set1)
print(set1)
print(set2)

set9 = set1-set2
print(set9)

#Finding symmetric differences of sets
set10 = set1.symmetric_difference(set2)
print(set10)

set11 = set1 ^ set2
print(set11)

#Finding subset
set12 = set([1,2,3,4,5,6])
set13 = set([1,2,3])
print(set13.issubset(set12))
print(set12.issuperset(set13))


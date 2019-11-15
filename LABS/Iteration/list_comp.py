# List comprehension
# Good way to create a new list by performing an
#  operation on each item in an existing list

# Separating letters in a string
chars = []
for ch in 'Daniel':
    chars.append(ch)
print(chars)

######Output expression <input sequence>
print([ch for ch in 'Daniel'])

squares = [x*x for x in range(11)]

print(squares)


#list of tuples
list1 = [1, 2, 3]
list2 = ['a','b','c']

combined_list = [(x,y) for x in list1 for y in list2]
print(combined_list)

# list comp with optional predicate
evens = [x for x in range(21) if x % 2 == 0]
print(evens)

# list comp with multiple optional predicate (AND)
byFiveTwo = [x for x in range(21) if x % 2 == 0 if x % 5 == 0]
print(byFiveTwo)

# list comp with multiple optional predicate (AND)
byFiveTwo = [x for x in range(21) if x % 2 == 0 or x % 5 == 0]
print(byFiveTwo)

obj = ['Even' if i % 2 == 0 else "Odd" for i in range(30) if i % 5 == 0]
print(obj)

# flatten a list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)

nums = [1,2,3,4]
string = ['a','b','c','d']
# I want a letter , number pair for each letter in str and each number in nums

mylist = []
for letter in string:
    for num in nums:
        mylist.append((letter,num))
print(mylist)

# the list comprehention way
mylist2 = [(letter, num) for letter in string for number in nums]
print(mylist2)

# Set comprehension
nums = [1,2,1,1,9,3,4,5,2,7,6,7,8,9]
mySet = set()
for n in nums:
    mySet.add(n)
print(mySet)

mySet2 = {n for n in nums}
print(mySet2)

# Dictionary comprehension
names = ['Bruce','Clark','Peter','Logan','Wade']
secrets = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

#I want a dict{'name':'secret} for each name, secret in zip names, secret
my_dict = {}
for name, secret in zip(names, secrets):
    my_dict[name] = secret
print(my_dict)

my_dict = {name:secret for name, secret in zip(names, secrets)}
print(my_dict)

# Generator Expression
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen =gen_func(nums)

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

my_gen2 = (n*n for n in nums)
for i in my_gen2:
    print(i)
# Filter
# Takes in two arguments, function and iterable,
#  and returns items in the list that are True

def isPrime(x):
    for n in range(2, x):
        if x % n ==0:
            return False
    return True
    
filterObject = filter(isPrime, range(100))
print('Prime numbers between 1-10: ', list(filterObject))

# Filter applied with lambda
filterObject2 = filter(lambda x: x % 2 == 0, range(10))
print(list(filterObject2))

# Filter on a random list w/out a function (None is not a function)
randomList = [1, 'a', 0, False, True, '0']
filteredList = filter(None, randomList)

print('The filtered elements are ')
for element in filteredList:
    print(element)

# filter for words in a list that contain the letter 'e'
words = ['list', 'done', 'exit']
print(list(filter(lambda x: 'e' in x, words)))




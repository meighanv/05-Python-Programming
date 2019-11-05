#Dictionaries

#Creating a dictionary
phonebook = {'David': '555-6644', 'Chris':'555-1234', 'Katie': '555-2222', 'JoAnn': '555-1122'}

#Adding an element
phonebook['David'] = '555-5555'

#Delete a key/value pair
del phonebook['David']

#Length of dictionary
length = len(phonebook)

#Using update
phonebook.update({'David': '555-6644', 'Chris':'555-1234'})

phonebook2 = {'Jim':'555-9900'}
phonebook.update(phonebook2)

#A neater way to define a dictionary. Data types can be mixed as well (within keys and values)
test_scores = { 'Kayla': [88,92,55],
                'Luis': [95, 74, 91],
                'Sophie': [70,75,78] 
                }
kayla_scores = test_scores['Kayla']
#Getting a specific element of the list value
kayla_scores[1]

#Empty dictionary 
empty_dict = {}
empty_dict[1] = 'This is a value'

#Iterating through a dictionary
for key in phonebook:
    print(key)

for key in phonebook:
    print(key, phonebook[key])

#makes the dict empty
#phonebook.clear()

#get method
#dictionary.get(key, default)
value = phonebook.get('Katie', 'Entry not found.')

value2 = phonebook.get('David', 'Entry not found.')

#items method
print(phonebook.items())

#Key method
for key in phonebook.keys():
    print(key)

for value in phonebook.values():
    print(value)

#Pop method - takes value out of dictionary (removes) the key-value pair, and returns the value ONLY
phonebook.pop('Chris', "Entry not found")

#pop item method - takes the latest key-value pair out of the dictionary, and returns the key-value pair
key, value = phonebook.popitem()
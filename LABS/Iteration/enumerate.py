# enumerate()

# Iterates over different types of iterables 
# and returns both the index and the value of
#  each item.

# Enumerate over some names 
# ',start = X' will determine the index where
#  the enumeration starts
names = ['Daniel', 'Joe','jim','Travis']
print(list(enumerate(names, start = 4)))
for name in enumerate(names, start = 6):
    print(name)

# This allows us to control what is printing
# Can shorten the ' start = ' command with just
#  the number
for count, item in enumerate(names):
    print(count, item)

my_string = 'Enumerating is Powerful'
for idx, ch in enumerate(my_string):
    print(f'Index is {idx} and character is {ch}')

# dictionary comprehension w/ enumerate
my_dict = {k: v for k, v in enumerate(names)}
print(my_dict) 
import datetime

today = datetime.datetime.now()
# Presenting this information to the user
print(str(today))

# Repr is more for developer mindset
print(repr(today))

# An accessor method (or getter) is something that gets attributes of the objects
# A mutator method (or setter) changes the attribute of an object instance

# Cannot use a name for a class that matches a keyword
# Get keywords
import keyword
keyword.kwlist()


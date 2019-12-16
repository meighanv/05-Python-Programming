# Used to execute existing OS commands
import os

# Used to execute existing OS commands
import sys

# Used to encode text
import io

#Creating a data variable to execute a command and store the returned data as a tuple
filename = ''
options= '-l'
command = 'ls ' + options + " " + filename
data = os.popen(command)

output = str(data.read())
#formatted = io.TextIOWrapper(output, encoding = 'utf-8')

print(output)

# Leverage sys library to get the size of the output in bytes
size = sys.getsizeof(str(output))
print(f'The size of the output is {size} bytes')



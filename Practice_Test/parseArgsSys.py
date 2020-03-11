#!/usr/bin/python3
'''

Write a python script that parses one or more command line items. The items may be
convertable to either an int or float. If not, assume it is a string.

For example, you should be able to run your file from the command line like:

testfile.py 1 3 4.7 hello 5.4 2 hi

In the above example, there are seven arguments to parse and process.

The script should create a variable to store a running total of an integer.

The running total will be increased accordingly as you parse each
argument from the command line:
   1. If the argument is convertable to an int, add the int to the total
   2. Otherwise, if the argument is converatable to a float, round the float
      to an int and add it to total.
   3. If the argument is convertable to neither an int or float, obtain the
      length of the string and add the length to the total.
      
After all command line arguments have been parsed, write the single total to a file
called output.txt



'''

import sys
sys.argv.pop(0)
#print(len(sys.argv))

#print(sys.argv)
filename = "output.txt"

total = 0
for i in sys.argv:
   try:
      i = float(i)
      i = int(round(i))
      total += i
   except ValueError:
      total += len(i)
   
#print(total)

f = open(filename, "w")
f.writelines(str(total))
f.close()

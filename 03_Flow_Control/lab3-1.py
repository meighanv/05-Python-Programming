## This is a program that prints simple, personal information
## Setting up the variables that will be passed as strings to print
name = 'Hans Grueber'
address = '2121 Avenue of the Stars, Los Angeles, CA 90067'
phone = '(213) 974-3211'
mos = '0301, GG-12'

#Printing each variable in a statement with the various string formatting
print("Name: %s" % name)
print(f"Address: ", address)
print("Phone: {} ".format(phone))
print("MOS: %s" % mos)
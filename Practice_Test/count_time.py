'''
Write the function find_culprits that receives the name of a file.
The function will open and read the file.
The file contains a list of user ids and number of minutes their
login session has been idle. The file can contain multiple session entries
of the same user id.  The format of the file is:  userid, mins

Example:

jschmo, 22
haaron, 12
haaron, 7
jschmo, 17

The function should find the (up to) top five users with the most total idle time and 
save them in order (highest to lowest) in a list of lists.  Each list item in the list will contain a userid
and number of mins as an integer in that order.

Example  [["jschmo",39],["haaron",19]]

Write no more than the top five users to the list handliing the case where there may not be five total
users.

If the file cannot be opened, return the string "BAD_FILE"

For this exercise all data in the file has valid format/content.

If the file process successfully, return the list of lists of users

'''

# Define find_culprits function receiving fileName as an arg for a 
# file name
def find_culprits(fileName):
	# Try to read file; return BAD_FILE msg on error
	try:
		f = open(fileName, 'r')
		# Read the lines of the file to lines list 
		lines = f.readlines()
	except FileNotFoundError:
		return f'BAD_FILE'

	# Creating a temporary list to store each line as a nested list	
	usersList = []
	# Creating a list for just users
	users= []
	# Iterate through the lines from file
	for line in lines:
		# set temp user var to first element in line
		user = line.split(", ")[0]
		# set temp time var to second element in line
		time = int(line.split(", ")[1])
		# append current user to users list
		users.append(user) 
		# append user/time combination to usersList as nested list
		usersList.append([user, time])
	#convert users list into a set to make it unique
	users = set(users)
	# Creating a totalList variable to store users pair with total time
	totalList = []
	# iterate through the unique users list
	for user in users:
		# Set totalTime Accumulator
		totalTime = 0
		#iterate through each entry in usersList
		for entry in usersList:
			# if user matched the first line element ...
			if entry[0] == user:
				# add the second line element to the total
				totalTime += entry[1]
		# Append the user, totalTime pair to the totalTime list 
		totalList.append([user, totalTime])
	
	# call the list sort function using 'key' to sort by 
	# subelement 1 (time) first, then subelement 0 (name) 2nd
	# in reverse order
	totalList.sort(key = lambda x :(x[1], x[0]), reverse=True)
	# Setting an empty top 5 list 
	top5List = []
	# Iterating through first 5 elements in totalList
	for i in range(5):
		try:
			# Attempt to append list element i
			top5List.append(totalList[i])
		except IndexError:
			# but if it is out of range (less than 5 total users)...
			break
	#return the top 5 list
	return top5List

# good = [['bbergner', 46], ['rboone', 44], ['ecruz', 44], ['dfarr', 42], ['jwarren', 38]]
		
# small = [['ecruz', 44], ['rboone', 34], ['dgilles', 26], ['jwarren', 14]]

# for i in find_culprits('smallList.txt'):
# 	print(i)

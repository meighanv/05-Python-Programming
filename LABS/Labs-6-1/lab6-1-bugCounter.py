from functools import reduce

#Initializing constant array for days of the week
DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def main():
    #Setting empty array for bug collection numbers
    bugsCollected = []
    #Calls the collect bugs function to capture bug count for each day of the week
    collectBugs(bugsCollected)
    print('You have collected {} bugs this week!'.format(totalBugs(bugsCollected)))

def collectBugs(collection):
    for i in DAYS:
        #Each iteration calls the getBugs function for input collection 
        # and validation to append what is returned to the array passed in 
        collection.append(getBugs(i))

#Defining a function to take in a day passed by 
# for loop in collectBugs() as a question 
# and validate input as positive and numeric
def getBugs(day):
    bugs = input('How many bugs did you collect on {:s}:\n'.format(day))
    #Input validation checking numeric and a positive number
    while int(bugs) <= 0 and bugs.replace('.','').isnumeric() == False:
        bugs = input('Invalid input. How many bugs did you collect on {:s}:\n'.format(day))
    return int(bugs)

#Calculates the total bugs collected 
def totalBugs(bugs):
    # Replacing original function code with lambda function
    total = reduce((lambda x, y: x + y), bugs)
    # #Initialize total 
    # total = 0
    # #Loop through the bugs(array) to add to the total
    # for i in bugs:
    #     #Adding the value of i to total
    #     total += i
    return total

main()

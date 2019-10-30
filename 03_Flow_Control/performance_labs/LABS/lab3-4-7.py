#Defining constant dictionary for the amount of book purchased to the amount of points for the month
CLUB_POINTS = {'0': 0,
    '1': 5,
    '2': 15,
    '3': 30,
    '4': 60}

def main():
    #requesting user input for the number of books purchased
    numBooks = getBooks() 

    #References the constant dictionary to determine the amount of points awarded
    calcPoints(numBooks)

#Getting input for number of books bought    
def getBooks():
    #getting user input as string
    books = input('How many books did you buy last month:\n')
    #Input validation to ensure the books entered is greater than 0
    while int(books) < 0:
        books = input('How many books did you buy last month:\n')
    #Checking if the books purchase was more than four
    if int(books) > 4:
        #if it is more than four no more points can be earned, therefore we set the string to 4
        return '4'
    else:
        #Otherwise we return the string of the number of books to match a dictionary key
        return str(books)

def calcPoints(count):
    #Prints the points earned by looking up their string in the dict as the key 
    print('You have earned {} points this month!'.format(CLUB_POINTS[count]))

main()
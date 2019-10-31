#Defining main
def main():
    #Requesting user input for date
    year = getYear()
    month = getMonth()
    day = getDay(month,year)
    
    #Calling the isMagic function to check the date
    isMagic(month,day,year)

#defining function to get the month while incorporating some input validation
def getMonth():
    month = int(input('Please provide the month (in numerical form):\n'))
    while month < 1 or month > 12:
        month = int(input('Invalid response. Please provide the month (in numerical form, 1-12):\n'))
    return month

#defining function to get the month while incorporating some input validation
def getYear():
    year = (input('Please provide the 2-digit year:\n'))
    while int(year) < 0 or int(year) > 99:
        year = (input('Invalid response. Please provide the 2-digit year:\n'))
    return year

#defining the validation for days including the month of feb and the leap year
def getDay(m,y):
    day = int(input('Please provide the day of the month:\n'))
    if m == 2 and int(y)%4 == 0:
        while day < 1 or day > 29:
            day = int(input('Invalid respone for the month of February in a leap year. Please provide the day of the month:\n'))
    elif m == 2:
        while day < 1 or day > 28:
            day = int(input('Invalid respone for the month of February. Please provide the day of the month:\n'))
    elif (m < 8 and m % 2 == 0) or (m > 7 and m % 2 == 1):
        while day < 1 or day > 30:
            day = int(input('Invalid respone for the months of FEB, APR, JUN, SEP, and NOV. Please provide the day of the month:\n'))
    else:
        while day < 1 or day > 31:
            day = int(input('Invalid respone; days cannot be less than 1 or greater than 31. Please provide the day of the month:\n'))
    return day

#defining magic check function
def isMagic(m,d,y):
    #condition formula is the magic date calculation
    if m * d == y:
        #Displaying Magic message!
        print('{}/{}/{} is magic!'.format(m,d,y))
    else:
        #Displaying not magic message.
        print('{}/{}/{} is NOT magic. :-/'.format(m,d,y))

#Calling Main
main()
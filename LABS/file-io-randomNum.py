#Importing random library
import random

#defining main function
def main():
    #Getting filename from input for filename
    filename = input('Provide the new file name:\n')
    f = open(filename, 'w')
    writeRandNum(getCount(),f)

#Input validation for user input for the number of random numbers to write to the file
def getCount():
    #initializing numCount for while condition
    numCount = 0
    while numCount == 0:
        #Testing user input via try/except
        try:
            numCount = int(input('Provide the number of random numbers to put in file:'))
        except:
            print('A number was not provided')
    #Once through the successful try/except input is received return it to main 
    return numCount

#Takes the user input and the filename 
def writeRandNum(num,file):
    for i in range(num):
        file.write('{}\n'.format(random.randint(1,100)))

main()
#Importing random library
import random

#Defining main function
def main():
    #Getting filename from input for filename
    filename = input('Provide the new file name:\n')
    #Reads the file of filename 
    f = open(filename, 'r')
    #Recording file contents in array
    contents = f.readlines()
    #Selecting a random number from within the range of the count of numbers read into the array
    numSelected = random.randint(1,len(contents))
    #Create the array to store the numbers randomly selected from filename
    randFromFile = []
    #Function for selecting a random number (numselected) from contents to add to randFromFile
    getRandFromFile(numSelected,contents,randFromFile)
    #Displays the data from array randFromFile
    measureRand(randFromFile, numSelected, filename)

#Function loops num times to select a random number from contents to add to numArray 
def getRandFromFile(num,contents,numArray):
    for i in range(num):
        numArray.append(contents[random.randint(1,num)])

#Function to measure the randFromFile array; count, sum, and average of elements
def measureRand(randFromFile,numSelected,filename):
    total=0
    for num in randFromFile:
        total += int(num)
    print('{} numbers selected at random from {}.'.format(numSelected,filename))
    print('The total of the selected numbers was {}.'.format(total))
    print('The average of the selected numbers was {:.2f}'.format(int(total)/len(randFromFile)))

#Call main function
main()
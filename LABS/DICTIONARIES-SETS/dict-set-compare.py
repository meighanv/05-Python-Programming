#This is meant to take two files and compare them
def main():
    #Stores the lines of the file specified by the user
    source = readFile('Provide the name of the first file')
    source2 = readFile('Provide the name of the second file')
    
    #This calls the function to extract all the words from a file
    words = getWords(source)
    words2 = getWords(source2)
    
    #This stores the return of the function which casts the words list as a set, making all words unique.
    unique = getUnique(words)
    unique2 = getUnique(words2)
    
    #Printing the sets
    printSet('Here is the list of words for the first file',unique)
    print('\n\n')
    printSet('Here is the list of words for the second file',unique2)
    
    #Printing various set comparisons
    compareSets(unique,unique2)

#this simple takes an array and casts/returns it as a set
def readFile(prompt):
    #Getting filename from input for filename
    filename = input('{}: \n'.format(prompt))
    #Reads the file of filename 
    f = open(filename, 'r')
    #Recording file contents in array
    contents = f.readlines()
    f.close()
    return contents

#Gets the individual words and normalizes them (lowercase, no trailing or preceding punctuation)
def getWords(original):
    #Iterate through each line
    newlist = []
    for i in original:
        #Split the lines by spaces (a typical delimeter in English between words)
        line = i.split(' ')
        #Add the words in the line to the list.
        newlist += line
    #Clean up each word in the list, getting rid of . \n "" and ?
    cleanlist = []
    for i in newlist:
        i = i.replace('\n','').replace('.','').replace('!','').replace('?','').replace('"','').replace(',','').replace('\'','')
        #ensures than all words are lower case to ensure set is properly unique
        i = i.lower()
        cleanlist.append(i)
    return cleanlist

#Casts any list to a set and returns result to main
def getUnique(array):
    uniqueItems = set(array)
    return uniqueItems

#Printing sets
def printSet(prompt,theSet):
    print('{}:\n------------'.format(prompt))
    array = list(theSet)
    for i in sorted(array):
        print(i)

#Function for comparing sets (intersection, difference, xor )
def compareSets(set1,set2):
    print('The words common to both files are:')
    displaySet = set1.intersection(set2)
    for i in displaySet:
        print(i)
    print()
    print('Uncommon words only in the first file:')
    displaySet = set1.difference(set2)
    for i in displaySet:
        print(i)
    print()
    print('Uncommon words only in the second file:')
    displaySet = set2.difference(set1)
    for i in displaySet:
        print(i)
    print()
    print('Uncommon in either file:')
    displaySet = set1.symmetric_difference(set2)
    for i in displaySet:
        print(i)
    print()

main()
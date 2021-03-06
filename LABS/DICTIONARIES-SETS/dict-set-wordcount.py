#This program is to grab all the unique words in a file.
def main():
    
    #this is the dictionary to store a word count for each unique word
    wordcount = {}
    #Stores the lines of the file specified by the user
    source = readFile()
    #This calls the function to extract all the words from a file
    words = getWords(source)
    
    #This stores the return of the function which casts the words list as a set, making all words unique.
    unique = getUnique(words)
    
    countWords(wordcount,words,unique)
    print('Here is the count for each word in the file:')
    for i in wordcount:
        print('{}: {}'.format(i, wordcount[i]))

#this simple takes an array and casts/returns it as a set
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
        i = i.replace('\n','').replace('.','').replace('!','').replace('?','').replace('"','')
        #ensures than all words are lower case to ensure set is properly unique
        i = i.lower()
        cleanlist.append(i)
    return cleanlist

#Casts any list to a set and returns result to main
def getUnique(array):
    uniqueItems = set(array)
    return uniqueItems

def readFile():
    #Getting filename from input for filename
    filename = input('Provide the new file name:\n')
    #Reads the file of filename 
    f = open(filename, 'r')
    #Recording file contents in array
    contents = f.readlines()
    f.close()
    return contents

def countWords(wordCount,words,unique):
    for uni in unique:
        count = 0
        for word in words:
            if uni.lower() == word.lower():
                count += 1
        wordCount.update({uni: int(count)})



main()
def readFile():
    #Getting filename from input for filename
    filename = input('Provide the new file name:\n')
    #Reads the file of filename 
    f = open(filename, 'r')
    #Recording file contents in array
    contents = f.readlines()
    f.close()
    return contents

words = []
source = readFile()

for i in source:
    line = i.split(' ')
    for j in line:
        words += j.rstrip('\n')
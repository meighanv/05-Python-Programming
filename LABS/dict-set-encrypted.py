#Configuring the encryption dictionary
codebook = {}
alphanum ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
encoded = '098765432!@$#%^&*()_+=-][}{;\'":\\`~}]abcdefghijklmnopqrstuvwxyz'
for i in range(len(alphanum)):
    key = alphanum[i]
    value = encoded[i]
    codebook.update({key: value})

#Define main function
def main():
    #Calls the readFile function to read the content of user specified file into the variable
    original = readFile()
    #Runs the substitution function on the input text using the codebook dictionary
    substitution(original,codebook)

#Substitution function
def substitution(contents,codebook):
    #creates and opens encrypted.txt file in write mode
    newfilename = 'encrypted.txt'
    f = open(newfilename, 'w')
    #Empty list for strings to be written once encoded
    lines = []
    #Loop through lines..
    for i in contents:
        #setting an empty string to place substitution characters
        line = ''
        # ...to loop through each line character
        for j in i:
            #Checks character presence as a codebook key
            if j in codebook:
                #adds the value to the string
                line += codebook[j]
            else:
                #writes same character if not in codebook
                line += j
        #writes the encrypted line to the lines array 
        lines += line
    #Writes the list of lines to the file
    f.writelines(lines)
    f.close()
    
def readFile():
    #Getting filename from input for filename
    filename = input('Provide the new file name:\n')
    #Reads the file of filename 
    f = open(filename, 'r')
    #Recording file contents in array
    contents = f.readlines()
    f.close()
    return contents

main()
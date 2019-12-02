# This is a program to ask the user for a filename (text file)
#  and a string to remove to remove the line and write the output to
#  to  a file called reduced .txt user w/ the content with the line removed 



def getFileContent():
    # Setting an empty array for content for the while loop condition
    content = []
    
    # While the array (content) is empty, the user will be prompted
    while len(content) == 0:
        # The try/except for reading in the file
        try: 
            filename = input('Provide the name of the text file you wish to edit:\n')
            f = open(filename, 'r')
            # Store the lines of the file as an list of lines
            content = f.readlines()
            f.close()
            return content
        except FileNotFoundError:
            print(f'Your file, {filename} was not found.')

def removeLine(content):
    # Tracks if a count of matching lines found
    found = 0

    # makes a unique list of line as options for the user
    setOfLines = set(content)
    
    # Displays the unique lines
    for line in setOfLines:
        print(line)
    # Get user input for line to remove    
    remove = input('Type the line you would like to remove. Available lines above:\n')
    while remove+'\n' not in setOfLines:
        for line in setOfLines:
            print(line)
            remove = input('Line does not exist!\nType the line you would like to remove. Available lines above (case sensitive):\n')
    # Creating empty list for the list of non-matching lines
    newLines = []
    # Loops through the lines to add non-matching ones to new list
    for line in content:
        if line != remove+'\n' and line != remove:
            newLines.append(line)
    return newLines

def main():
    # getting the content of the file using the function
    content = getFileContent()
    # Passing content into the remove line function to return 
    # all non-matching lines as the new content to write
    newLines = removeLine(content)
    # opening a new file called removed.txt to write the output
    # preserving the original file 
    outFile = open('removed.txt','w')
    outFile.writelines(newLines)
    outFile.close()

main()
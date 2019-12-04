# This function is meant to read in the help text file to parse it into
#  helpObjects that are returned as a list

def parseHelp(filename):
    # Opening and reading the lines of the file
    f = open(filename, 'r')
    # This reads in each line as it's own list item
    contents = f.read()
    f.close()

    import re
    import helpClass
    # Repacking the file content as a single string to control how
    # Content is broken up later for proper parsing
 
    helpObjects = []
    pattern = re.compile(r'Python ([\w]+) library.[\*]+\n\nCopied from: [\w\:\/\.]+\n\n(Description\: [\n \(\)\,\.\'\:\/\w-]+)\n(Example 1 \- [\w\n \(\),\.\'\:\/]+)\n(Example 2 \- [\w\n \(\),\.\'\:\/]+)\n')
    matches = pattern.finditer(contents)  

    for match in matches:
        lib = match.group(1)
        desc = match.group(2)
        ex1 = match.group(3)
        ex2 = match.group(4)
        helpTemp = helpClass.HelpObject(desc, ex1, ex2, lib)
        helpObjects.append(helpTemp)
    return helpObjects




helpData = parseHelp(filename)
for i in helpData:
    print(i.getDesc())

'''
Write the function manipulateFile that receives four parameters:
  fileName - the name of a file that you will read/write/append to/from
  findWord - a word to search for in the file
  insertWord - a word that will be inserted in the file
  appendWord - a word that will be appended to the end of the file

The function should read the file in fileName and determine if the string in findWord exists in the file.  If it does
exist, insert a space and the string in insertWord immediately after the findWord.

For example, the file may contain the following text:

The quick brown fox jumped 

If findWord contained "quick" and the insertWord contained "sly", once processed the line in the file would have:

The quick sly brown fox jumped

The string in appendWord will simply be appended to the end of the file preceded by a space. For example, the end of the
file may contain:

over the lazy dog's back

if appendWord contains "fence", once processed the line in the file would have:

over the lazy dog's back fence

if the file in fileName does not exist, the function should return the string: "FILE_ERROR"
if the string in findWord does not exist in the file, the function should return the string: "WORD_NOT_FOUND"
and make no changes to the file.
otherwise, the function should return "SUCCESS"

NOTE: during your development, should the data files under test get corrupted, pristine copies are located in the
'original files' folder.  Simply make a copy and bring over into your working directory.

'''


def manipulateFile(fileName, findWord, insertWord, appendWord):
  try:
    f = open(fileName, 'r')
  except FileNotFoundError:
    return f"FILE_ERROR"
  lines = f.readlines()
  f.close()
  #print(lines)
  newlines = []
  found = False
  for i in lines:
    if (findWord in i):
      i = i.replace(findWord,findWord+" "+insertWord,1)
      found = True
    newlines.append(i)  
  if (found == False):
    return f"WORD_NOT_FOUND"
  #print(newlines)
  if (newlines[-1][-1] == "\n"):
    newlines[-1] = newlines[-1].replace(newlines[-1][-1], " "+appendWord)
  else:
    newlines[-1] = newlines[-1].replace(newlines[-1][-1], newlines[-1][-1]+" "+appendWord)
  #print(newlines)

  # Present for testing to protect existing files
  #outfile = "test.txt"
  f = open(fileName, "w")
  for i in newlines:
    f.writelines(i)
  f.close()

  return "SUCCESS"

#print(manipulateFile("names.txt", "Jake", "Jamie", "Bevis"))

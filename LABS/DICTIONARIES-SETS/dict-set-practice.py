"""
Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the 
courses meet. The dictionary should have the following keyvalue pairs:
​
Course Number (key) Room Number (value)
CS101               3004
CS102               4501
CS103               6755
NT110               1244
CM241               1411
​
The program should also create a dictionary containing course numbers and the names of
the instructors that teach each course. The dictionary should have the following key-value
pairs:
​
Course Number (key) Instructor (value)
CS101               Haynes
CS102               Alvarado
CS103               Rich
NT110               Burke
CM241               Lee
​
The program should also create a dictionary containing course numbers and the meeting
times of each course. The dictionary should have the following key-value pairs:
​
Course Number (key) Meeting Time (value)
CS101               8:00 a.m.
CS102               9:00 a.m.
CS103               10:00 a.m.
NT110               11:00 a.m.
CM241               1:00 p.m.
​
The program should let the user enter a course number, and then it should display the
course’s room number, instructor, and meeting time.
​
​
​
2. Capital Quiz
Write a program that creates a dictionary containing the U.S. states as keys and their capitals as values. 
(Use the Internet to get a list of the states and their capitals.) The program
should then randomly quiz the user by displaying the name of a state and asking the user
to enter that state’s capital. The program should keep a count of the number of correct and
incorrect responses. (As an alternative to the U.S. states, the program can use the names of
countries and their capitals.)
​
3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary to 
write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.
​
4. Unique Words
Write a program that opens a specified text file and then displays a list of all the unique
words found in the file.
Hint: Store each word as an element of a set
​
5. Word Frequency
Write a program that reads the contents of a text file. The program should create a dictionary in which the keys are the individual words found in the file and the values are the
number of times each word appears. For example, if the word “the” appears 128 times,
the dictionary would contain an element with 'the' as the key and 128 as the value.
The program should either display the frequency of each word or create a second file
containing a list of each word and its frequency
​
6. File Analysis
Write a program that reads the contents of two text files and compares them in the following ways:
• It should display a list of all the unique words contained in both files.
• It should display a list of the words that appear in both files.
• It should display a list of the words that appear in the first file but not the second.
• It should display a list of the words that appear in the second file but not the first.
• It should display a list of the words that appear in either the first or second file but not both.
Hint: Use set operations to perform these analyses.
"""
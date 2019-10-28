print("Please type a sentence:")
x = input()

wordCount = len(x.split(" "))
print("Sentence word count: " + str(wordCount))

charCount = len(x)
print("Sentence character count: " + str(charCount))

upperCount = 0
lowerCount = 0
for i in x:
    if i.isupper() == True:
        upperCount += 1
    else:
        if i.islower() == True:
            lowerCount += 1

print("Uppercase characters in sentence: " + str(upperCount))
print("Lowercase characters in sentence: " + str(lowerCount))
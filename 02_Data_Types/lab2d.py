print("Please input a string:")
x = str(input())

count = len(x) - 1
revStr = ''

while count >= 0:
    revStr += x[count].upper()
    count -= 1

print("Your string was " + x + ". your string reversed and capitalized is " + revStr + "!")


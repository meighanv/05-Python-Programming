import random

def main():
    filename = input('Provide the new file name:\n')
    f = open(filename, 'r')
    contents = f.readlines()
    numSelected = random.randint(1,len(contents))
    randFromFile = []
    getRandFromFile(numSelected,contents,randFromFile)
    measureRand(randFromFile, numSelected, filename)

def getRandFromFile(num,contents,numArray):
    for i in range(num):
        numArray.append(contents[random.randint(1,num)])

def measureRand(randFromFile,numSelected,filename):
    total=0
    for num in randFromFile:
        total += int(num)
    print('{} numbers selected at random from {}.'.format(numSelected,filename))
    print('The total of the selected numbers was {}.'.format(total))
    print('The average of the selected numbers was {:.2f}'.format(int(total)/len(randFromFile)))
main()
import random

def main():
    filename = input('Provide the new file name:\n')
    f = open(filename, 'w')
    writeRandNum(getCount(),f)
    
def getCount():
    numCount = 0
    while numCount == 0:
        try:
            numCount = int(input('Provide the number of random numbers to put in file:'))
        except:
            print('A number was not provided')
    return numCount

def writeRandNum(num,file):
    for i in range(num):
        file.write('{}\n'.format(random.randint(1,100)))

main()
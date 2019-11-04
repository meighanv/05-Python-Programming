def main():
    filename = input('Provide the new file name:\n')
    f = open(filename, 'w')
    name = getName()
    

def getName():
    name = input('Provide the player\'s name:\n')
    return name

def getScore(player):
    score = -55
    while score <= -50
        try:
            score = int(input('Provide score for {}'.format(player)))
        except:
            print('Incorrect input.')
            score =-55

def writeScore(file,name):
    score = getScore(name)
    


main()


import random

#define main
def main():
    lotto = []
    selectNum(lotto)
    showNum(lotto)

def selectNum(lotto):
    for i in range(7):
        lotto.append(random.randint(0,9))

def showNum(lotto):
    print('Your lottery numbers for this week are:\n')
    for i in lotto:
        print(i)

main()
#Defining the maximum number of numbers
CAP = 20

#define main
def main():
    numArray = []
    for i in range(CAP):
        getInput(numArray)
    measureList(numArray)
    print(numArray)
def getInput(array):
    userInput = -5000
    while userInput == -5000:
        try:
            userInput = int(input('Please provide an integer value:\n'))
            array.append(userInput)
        except:
            userInput = -5000
            print('That was not a number.')

def measureList(array):
    total = 0
    for i in array:
        total += i
    print('Total months of array in data: {}'.format(len(array)))
    print('Total array: {:.2f} inches'.format(total))
    print('Average monthly array: {:.2f}'.format(total/len(array)))
    print('The maximum array was {}'.format(max(array)))
    print('The minimum array was {}'.format(min(array)))

main()

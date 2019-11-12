import random

capitols = {'Virginia':'Richmond',
            'Texas':'Austin',
            'New York':'Albany',
            'Maryland':'Baltimore'}


def main():
    correct = 0
    incorrect = 0
    count = 0
    while count < 3:
        states = getStates(capitols)
        state = quizChoice(states)
        if getAnswer(capitols,state) == 1:
            correct += 1
        else:
            incorrect += 1
        count += 1
    print('You got {} correct!'.format(correct))
    print('You got {} incorrect!'.format(incorrect))

def getStates(dictionary):
    array = list(dictionary.keys())
    return array

def quizChoice(states):
    state = states[(random.randint(0,len(states)-1))]
    print('What is the capitol of {}?'.format(state))
    return state

def getAnswer(states,state):
    score = 0
    answer = capitols[state]
    userInput = input()
    if userInput.lower() == answer.lower():
        score += 1
    return score


main()
import random
import pickle
from os import path

print('Let\'s play Hangman! There is a word that you must \nguess by guessing letters one at a time. If the\n letter is present is will be populated. If not,\n then your person will start to be hung. \n 6 wrong questions and it\'s GAME OVER!')

def main():
    usedAlpha = []
    death = 0
    word = getWord()
    answer = splitWord(word)
    guess = initGuess(word)
    state = False
    compAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    gameModes = ['c', 'i']
    mode = 'g'
    hang = loadHang()
    while mode.lower() not in gameModes:
        mode = input('Which mode would you prefer:\n- (C)omputer Solo Mode\n- (I)nteractive Mode\n')
    if mode == 'i': 
        name = input('Please provide your name to track your scores:\n')
        scoreData = getProfile(name.lower())
        deathState(hang, death)
        while state == False:
            print('You have {} wrong guesses remaining.'.format(6 - death))
            death += userGuess(usedAlpha, answer, guess)
            deathState(hang, death)
            state = checkWin(death, answer, guess, state)
        updateScores(scoreData, name, death)
    elif mode == 'c':
        while state == False:
            print('Computer has {} wrong guesses remaining.'.format(6 - death))
            death += compGuess(usedAlpha, answer, guess, compAlpha)
            deathState(hang, death)
            state = checkWin(death, answer, guess, state)


def getWord():
    with open("wordbank.txt", encoding = 'utf-8') as bank:
        words = bank.readlines()
        word = (words[random.randint(0,len(words)-1)]).lower().replace('\n','')
    bank.close()
    return word.lower()

def splitWord(word):
    answer = []
    for i in word:
        answer.append(i)
    return answer

def initGuess(word):
    guess = []
    for i in word:
        guess.append('_')
    return guess

def userGuess(usedAlpha, answer, guess):
    hit = 0
    for i in guess:
        print(i ,end=' ')
    print('\n')
    print('Letters used: ', usedAlpha)
    letter = input('Please guess a letter:\n')
    while letter.isalpha() == False or letter.lower() in usedAlpha:
        letter = input('Please guess a letter:\n')
        print('Letters used: ', usedAlpha)
    usedAlpha.append(letter.lower())
    if letter in answer:
        positions = getIndexPositions(answer, letter)
        for i in positions:
            #replaces the existing element with the marker
            guess[i] = letter.lower()
        print('Yes!')
    else:
        hit = 1
        print('Nope!')
    return hit

def checkWin(death, answer, guess, state):
    state = False
    if death == 6:
        print('GAME OVER! YOU DIED!')
        state = True
    elif answer == guess:
        print('GAME OVER! YOU WIN!')
        state = True
    else:
        state = False
    return state

def getIndexPositions(listOfElements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    indexPosList = []
    indexPos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            indexPos = listOfElements.index(element, indexPos)
            # Add the index position in list
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
    return indexPosList

def compSelect(compAlpha,usedAlpha):
    compIndex = random.randint(0,len(compAlpha)-1)
    compChoice = compAlpha[compIndex]
    print('The computer chooses \'{}\'....'.format(compChoice))
    compAlpha.remove(compChoice)
    return compChoice

def compGuess(usedAlpha, answer, guess, compAlpha):
    hit = 0
    for i in guess:
        print(i ,end=' ')
    print('\n')
    print('Letters used: ', usedAlpha)
    letter = compSelect(compAlpha, usedAlpha)
    usedAlpha.append(letter.lower())
    if letter in answer:
        positions = getIndexPositions(answer, letter)
        for i in positions:
            #replaces the existing element with the marker
            guess[i] = letter.lower()
        print('Yes!')
    else:
        hit = 1
        print('Nope!')
    return hit

def getProfile(name):
    scoreFile = 'scores.dat'
    scoreData = {}
    if path.exists(scoreFile):
        with open(scoreFile, 'rb') as scores:
            end_of_file = False
            while end_of_file == False:
                try:
                    #unpickle next object
                    scoreData = pickle.load(scores)
                except EOFError:
                    #Set flag to indicate EOF reached
                    end_of_file = True
        print('Your score history:\n{}\n'.format(scoreData[name]))
    else:
        scoreData = {name: {'win':0, 'loss':0}}
        with open(scoreFile, 'wb') as scores:
            pickle.dump(scoreData, scores) 
    
    if name.lower() not in scoreData:
            scoreData.update({name: {'win':0, 'loss':0}}) 
    
    return scoreData

def updateScores(scoreData, name, death):
    scoreFile = 'scores.dat'
    if death >= 6:
        scoreData[name]['loss'] += 1
    else:
        scoreData[name]['loss'] += 1
    with open(scoreFile, 'wb') as scores:
        pickle.dump(scoreData, scores)
    
def loadHang():
    filename = 'death.txt'
    with open(filename, 'r') as hang:
        image = hang.readlines()
    return image

def deathState(hang, death):
    start = death * 6
    stop = start + 6
    step = 1
    for i in range(start,stop,step):
        print(hang[i].rstrip('\n'))
    print('\n')
main()


"""
Task:
    Your task is to implement the Hangman game in Python.
​
Program Specifications:
    1) Output a brief description of the game of hangman and how to play
    2) Ask the user to enter the word or phrase that will be guessed (have a friend enter the phrase 
        for you if you want to be surprised)
    3) Output the appropriate number of dashes and spaces to represent the phrase (make sure it’s clear 
        how many letters are in each word and how many words there are)
    4) Continuously read guesses of a letter from the user and fill in the corresponding blanks if the 
        letter is in the word, otherwise report that the user has made an incorrect guess.
    5) Each turn you will display the phrase as dashes but with any already guessed letters filled in, 
        as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
    6) Your program should allow the user to make a total of k=6 guesses.
​
Assignment Notes:
If the letter has already been guessed, output a message to the player and ask for input again.
If the guess entered is not an alphabetic letter, output a message and ask for input again.
​
If the letter is present in the word to be guessed, fill in the blanks appropriately with this particular letter. 
If the complete name has been guessed, the game is over  - player wins the game.  Output a message telling the 
player they have won and quit the game.
​
If the letter/digit is not present in the word to be guessed, give a message to the player indicating that the 
guess is incorrect and remaining number of chances is one less. If remaining number of chances is 0 (zero), 
the game is over  - player loses the game. Output a message that they have lost and what the correct word was.  Quit the game.
​
Bonus:
    You can do one or both of the following:
​
    1) Using a file:
    Instead of asking for user input for the word, make a word bank in a file named hangman_words.txt. 
    Read in the contents of the file and choose a word at random.
​
    2) Forever alone option:
    You enter the word (or it is randomly chosen from the word bank) and have the computer try to guess the letters.
​
    3) Add some more functionality: 
        - Persist user profiles with scores
        - Prompt for which user is playing
        - Ask if the user wants to play a set of games
        - Build a leader board
        
    Have fun, get creative, and demonstrate what you've come up with.
"""

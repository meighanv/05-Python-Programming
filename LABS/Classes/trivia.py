"""8. Trivia Game
    In this programming exercise you will create a simple trivia game for two players. The program will 
    work like this:
        • Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
        should be a total of 10 questions.) When a question is displayed, 4 possible answers are
        also displayed. Only one of the answers is correct, and if the player selects the correct
        answer, he or she earns a point.
        • After answers have been selected for all the questions, the program displays the number
        of points earned by each player and declares the player with the highest number of points
        the winner.
    To create this program, write a Question class to hold the data for a trivia question. The
    Question class should have attributes for the following data:
        • A trivia question
        • Possible answer 1
        • Possible answer 2
        • Possible answer 3
        • Possible answer 4
        • The number of the correct answer (1, 2, 3, or 4)
    The Question class also should have an appropriate __init__ method, accessors, and
    mutators.
    The program should have a list or a dictionary containing 10 Question objects, one for
    each trivia question. Make up your own trivia questions on the subject or subjects of your
    choice for the objects.
"""

# This style of import corrected an issue reading in the dat 
# file for an AttributeError in __main__ 
from questions import Question
import random
import pickle

#Define main function
def main():
    # Set filename for question bank
    filename = 'qbank.dat'

    # Call the readData function to pickle in the data
    qbank = readData(filename)
    
    # setting the question bank index list to keep track of questions 
    # asked
    qindex = []

    # Loops through all questions in question bank to create a list of indexes
    for i in range(len(qbank)):
        qindex.append(i)
    
    # Sets the turn at 1.
    # Used for tracking the turn and player's turn
    turn = 1

    # Initialize variables to track players scores
    p1score = 0
    p2score = 0

    # Loops through all questions in the question bank
    for i in range(len(qbank)):

        # Calls the askQuestion function and returns the result of 
        # 1 or 0 (correct or incorrect) for addition to player score
        result = askQuestion(turn, qbank, qindex)

        # Determines which player to credit the result to
        if turn % 2 == 1:
            p1score += result
        else:
            p2score += result
        # Increments the turn
        turn += 1
    # Prints scores
    print(f'\n\nPlayer 1 score:\n{p1score}\n\nPlayer 2 score:\n{p2score}\n')
    # Determines and prints winner
    if p1score > p2score:
        print('Player 1 Wins!!!')
    elif p2score > p1score:
        print('Player 2 Wins!!!')
    else:
        print('Everybody Wins!!!')

# Define ask question function
def askQuestion(turn, qbank, qindex):
    # Checks whose turn it is
    if turn % 2 == 1:
        print('Player 1\'s turn:')
        # initializes prompt variable
        prompt = -1
        # Random selection validation mechanism while keeping 
        # track using the qindex
        while prompt not in qindex:
            # Generates random number within the length 
            # of the qbank
            prompt = random.randint(0,len(qbank)-1)
        # Prints the question by calling the printQuestion function
        printQuestion(qbank, prompt)

        # Storing the result of checkAnswer in points (T/F)
        points = checkAnswer(qbank, prompt)

        # Removes the choice from the qindex so that 
        # the choice (and the question) cannot be selected 
        # again
        qindex.remove(prompt)

        # Based on the state of points it returns 1 or 0
        if points == True:
            return 1
        else:
            return 0

    # Same logic as the 'if', but for player two    
    else:
        print('Player 2\'s turn:')
        prompt = -1
        while prompt not in qindex:
            prompt = random.randint(0,len(qbank)-1)
        printQuestion(qbank, prompt)
        points = checkAnswer(qbank, prompt)
        qindex.remove(prompt)
        if points == True:
            return 1
        else:
            return 0

def printQuestion(bank, prompt):
    print(f'{bank[prompt].get_question()}')
    print(f'1. {bank[prompt].get_answer1()}')
    print(f'2. {bank[prompt].get_answer2()}')
    print(f'3. {bank[prompt].get_answer3()}')
    print(f'4. {bank[prompt].get_answer4()}')

def checkAnswer(bank, prompt):
    correct = False
    userAns = input('What is your answer? (Please type 1, 2, 3, or 4)\n')
    while int(userAns) not in range(1,5):
        userAns = input('What is your answer? (Please type 1, 2, 3, or 4)\n')
    if bank[prompt].get_correct() == userAns:
        correct = True
    return correct

def readData(filename):
    # Opening the file in read mode
    emp_file = open(filename, 'rb')
    # Setting EOF to false
    end_of_file = False
    #Setting while loop to get each object in binary file
    while not end_of_file:
        try:
            #unpickle next object
            dictionary = pickle.load(emp_file)
            return dictionary
        except EOFError:
            #Set flag to indicate EOF reached
            end_of_file = True
    emp_file.close()

main()
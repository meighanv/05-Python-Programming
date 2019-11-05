#define board
board = [['1','2','3'],['4','5','6'],['7','8','9']]
#define main function
def main():
    #Prints welcome
    print('Let\'s play Tic-Tac-Toe')
    #Initializes move counter for determining the turns and marker
    moveNum = 1 
    #An array of possible moves used to track move history
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #A while loop to go through all possible moves unless there is a winner first
    while moveNum <= len(moves):
        #Calls method to print board's current state
        printBoard(board, moveNum)
        #Calls function to get player move taking into account move history and current board state
        getMove(board,moveNum,moves)
        #Calls function to check win conditions
        winner = checkBoard(board)
        #checks the winner array to determine who has one if there is a winner
        if winner[0] == True:
            print('Player \'X\' is the winner')
            break
        elif winner[1] == True:
            print('Player \'O\' is the winner')
            break
        moveNum += 1
    #If no winner has been determined by the time the while loop ends the game assumes a tie    
    print('This game was a tie')
    

#The board printing function
def printBoard(board, moveNum):
    #Uses moveNum to determine whose turn it is for the prompt
    if moveNum % 2 == 1:
        print('X\'s turn to move:')
    else:
        print('O\'s turn to move:')
    #prints each row in the matrix
    for row in board:
        print(row)

#Gets move input with input validation
def getMove(board,moveNum,moves):
    #Sets the marker based on moveNum
    if moveNum % 2 == 1:
        marker = 'X'
    else:
        marker = 'O'

    #Initializes 'place' for while loop
    place = 'z'
    #Checking to see if the input is numeric for loop sentinel value
    while place.isnumeric() == False:
        #Take in input for 'place'
        place = input('Where would you want to place your \'{}\'?\n'.format(marker))
        #Tries to force it to an integer which is necessary after input
        try:
            #Nested while loop to ensure that the input exists in the valid available moves
            while int(place) not in moves:
                place = input('Invalid input of {}. Where would you want to place your \'{}\'?\n'.format(place, marker))
        except ValueError:
            #An error that shows them their input is invalid with available options
            print('Input must be a number in ', moves)
            place = input('Where would you want to place your \'{}\'?\n'.format(marker))
        
    #A for loop that checks each row...
    for row in board:
        #... for the presence of the user's input to get it's index
        if place in row:
            moveIndex = row.index(place)
            #replaces the existing element with the marker
            row[moveIndex] = str(marker)
            #removes the selected move from the list of possibilities
            moves.remove(int(place))

#the function to check win conditions
def checkBoard(board):
    #Defining each winning line on the 3x3 board
    topRow = [board[0][0],board[0][1],board[0][2]]
    midRow = [board[1][0],board[1][1],board[1][2]]
    botRow = [board[2][0],board[2][1],board[2][2]]
    leftCol = [board[0][0],board[1][0],board[2][0]]
    midCol = [board[0][1],board[1][1],board[2][1]]
    rgtCol = [board[2][0],board[2][1],board[2][2]]
    tlbrDiag = [board[0][0],board[1][1],board[2][2]]
    bltrDiag = [board[2][0],board[1][1],board[0][2]]
    #A list of lists making up the win conditions
    winCons = [topRow, midRow, botRow, leftCol, midCol, rgtCol, tlbrDiag, bltrDiag]
    #Booleans for X wins or O wins 
    xWin = False
    oWin = False
    #Loops through each win condition 
    for line in winCons:
        #Setting the counters for 'x' or 'o'
        xCount = 0
        oCount = 0
        #loops through each element in the win condition
        for j in line:
            #checks for 'X' and increments if it exists
            if j == 'X':
                xCount += 1
            #checks for 'O' and increments if it exists
            elif j == 'O':
                oCount += 1
        #If either of these counts reaches three then the win condition is met and the boolean is set to true
        if xCount == 3:
            xWin = True
        elif oCount == 3:
            oWin = True
    #return win condition state to main
    return xWin, oWin
    

main()
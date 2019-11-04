#define board
board = [['1','2','3'],['4','5','6'],['7','8','9']]
def main():
    print('Let\'s play Tic-Tac-Toe')
    moveNum = 1 
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while moveNum <= len(moves):
        printBoard(board, moveNum)
        getMove(board,moveNum,moves)

        moveNum += 1
    

def printBoard(board, moveNum):
    if moveNum % 2 == 1:
        print('X\'s turn to move:')
    else:
        print('O\'s turn to move:')
    for row in board:
        print(row)



def getMove(board,moveNum,moves):
    if moveNum % 2 == 1:
        marker = 'X'
    else:
        marker = 'O'
    place= input('Type the number where you would like to place {}:'.format(marker))
    for row in board:
        try:
            int(place) in moves
            moveIndex = row.index(place)
            row[moveIndex] = str(marker)
            moves.remove(place)
        except:
            print('Invalid Move')

main()
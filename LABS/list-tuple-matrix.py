import random
def main():

    ROWS = 4
    COLS = 4
    matrix = []
    makeMatrix(matrix)
    printMatrix(matrix)

def makeMatrix(matrix):
    for r in range(ROWS):
        matrix.append([random.randint(0,1)])
        for c in range(COLS-1):
            matrix[r].append(random.randint(0,1))


def printMatrix(matrix):
    for row in matrix:
        for i in row:
            print(i, end='')
        print()

def sumRow(row):
    total = 0 
    for i in row:
        total += i
    return total

def sumCol(matrix, rows, cols):
    for i in range(cols):
        for j in range()

def largestRow(matrix):
    largest = -1
    for i in range(ROWS):
        if sumRow(i) > largest:
            largest = sumRow(i)
            largestIndex = i
    return largestIndex 




print('The largest row index: {}'.format(maxRow))
print('The largest column index: {}, {}'.format(maxRow,maxCol))


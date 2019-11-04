import random

ROWS = 4
COLS = 4
matrix = []
for r in range(ROWS):
    matrix.append([random.randint(0,1)])
    for c in range(COLS-1):
        matrix[r].append(random.randint(0,1))


maxRow = matrix.index(max(matrix))
maxCol = matrix[maxRow].index(max(matrix[maxRow]))


for row in matrix:
    print(row)

print('The largest row index: {}'.format(maxRow))
print('The largest column index: {}, {}'.format(maxRow,maxCol))


def main():
    # Asking user for the number of rows and columns
    rows = getDimension('rows')
    cols = getDimension('columns')
    # Create and return a 3x4 matrix
    matrix = createMatrix(rows,cols)
    # Displays matrix for user to confirm the grid
    for row in matrix:
        print(row)

    # Find largest and coordinates
    # and print the info
    largest = findLargest(matrix)
    print(f'Largest number: {largest[0]}')
    print(f'Coordinates: {largest[1]}')

def createMatrix(rows,cols):
    matrix = []
    for row in range(rows):
        # Creating empty list for the row for each column element
        #  to be written to
        contents = []
        for col in range(cols):
            valid = False
            while valid == False:
                try:
                    # Appending successful try to contents for row element
                    contents.append(float(input('Please provide a number:')))
                    valid = True
                except ValueError:
                    print('Error: This is a non-number input!')
        # Writing the completed row
        matrix.append(contents)
    return matrix

def findLargest(matrix):
    largeNum = 0
    largeCoord = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > largeNum:
                largeNum = matrix[row][col]
                largeCoord = [row, col]
    return largeNum,largeCoord

def getDimension(dimension):
    valid = False
    while valid == False:
        try:
            # getting input for dimension as dim
            dim = int(input(f'Please provide a number {dimension} for your matrix:'))
            valid = True
        except ValueError:
            print('Error: This is a non-integer input!')
    return dim
main()
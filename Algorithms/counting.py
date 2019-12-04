# This prints number of iterations for problem sizes that double
# using a single loop

problemSize = 1000

for count in range(5):
    # Accumulator for the number of instructions 
    number = 0
    # Start of Algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1
    #End of Algorithm
    print(f'{problemSize} - {number}')
    problemSize *= 2
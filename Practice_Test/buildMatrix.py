def buildMatrix (rows, cols):
    # set midpoint variable for the odd square matrix situation
    midpoint = 0
    
    # Identify if parameters define a square matrix
    if (rows == cols):
        # Checking to see if the dimensions are odd
        if (rows%2 != 0):
            #Setting the midpoint variable to be an integer value of 
            #dimension divided by two which will put it right on the midpoint
            #since counting starts at 0
            midpoint = int(rows/2)
    
    #Create empy matrix to which we can append data
    matrix = []
    # Iterating through the range rows
    for r in range(rows):
        #createing an empty row list to which we append column elements
        row = []
        # Iterating through the size of columns
        for c in range(cols):
            #Checking the square midpoint condition
            if (r == c and r == midpoint and midpoint != 0):
                #If it checks out, then place a '1' in the element
                row.append(1)
            #Otherwise ...
            else:
                # Append the appropriate value
                row.append(r*c)
        #append the row list to the matrix list
        matrix.append(row)
                
    return matrix

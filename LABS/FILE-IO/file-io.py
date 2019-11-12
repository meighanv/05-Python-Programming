def main():
    '''#WRITE TO A FILE
    filename = 'C:\\Users\\student\\Documents\\names.txt' 
    f = open(filename, 'w')

    f.write('name 1\n')
    f.write('name 2\n')
    f.write('name 3\n')

    f.close()
    '''

    '''
    #READ FROM A FILE
    filename = 'C:\\Users\\student\\Documents\\names.txt' 
    f = open(filename, 'r')
    f_contents = f.read()
    f.close()
    print(f_contents)
    '''

    """ #READ A LINE FROM FILE
    filename = 'C:\\Users\\student\\Documents\\names.txt' 
    f = open(filename, 'r')
    #Readline reads the line then moves the pointer in the file to next line
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    #Strips characters
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    
    f.close()
    
    print(line1, end='')
    print(line2, end='')
    print(line3, end='') """

    """ #APPEND FILE
    filename = 'C:\\Users\\student\\Documents\\names.txt' 
    f = open(filename, 'a')
    f.write('NewName 1\n')
    f.close() """
""" 
    #WRITING TO SALES
    filename = 'C:\\Users\\student\\Documents\\sales.txt' 
    f = open(filename, 'w')
    f.write('1000.0\n2000.0\n3000.0\n4000.0\n5000.0\n')
    f.close() """

    
    filename = 'C:\\Users\\student\\Documents\\sales.txt' 
    f = open(filename, 'w')
    f.close()
main()
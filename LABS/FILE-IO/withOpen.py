filename = 'C:\\Users\\student\\Documents\\names.txt'
with open(filename,'r') as file:
    size_to_read = 3
    fcontents = file.read(size_to_read)
    print(fcontents)
def main():
    filename = input('Provide the name of a file:\n')
    f = open(filename, 'r')
    a = f.readlines()
    f.close()
    print('Your file {} has {} names.'.format(filename, len(a)))
    
main()
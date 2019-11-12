def main():
    filename = input('Provide the name of a file:\n')
    f = open(filename, 'r')
    a = f.readlines()
    lineNum = 1
    for i in a:
        print('{}. {}'.format(lineNum, i, end=''))
        lineNum += 1
    
main()
def main():
    f = getFilename()
    if f != '':
        a = f.readlines()
        f.close()
        getTotal(a)

def getFilename():
    try:
        filename = input('Provide the name of a file:\n')
        return open(filename, 'r')
    except IOError:
        print('The file {} is not found.'.format(filename))
        return ''

def getTotal(a):
    total = 0
    for i in a:
        try:
            total += int(i)
        except:
            print('This line does not contain a number.')
    print('The total of the numbers is {}.'.format(total))
    #This statement will satisfy the number average as well
    print('The average of the numbers is {:.2f}.'.format(total/len(a)))

    
main()
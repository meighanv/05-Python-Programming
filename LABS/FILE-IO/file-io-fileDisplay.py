#Read data from a file
def main():
    filename = 'C:\\Users\\student\\Documents\\numbers.txt'
    f = open(filename, 'r')
    for i in f.readlines():
        print(i, end='')

main()

def main():
    filename = input('Enter the filename: \n')

    try:
        infile = open(filename, 'r')

        contents = infile.read()

        print(contents)

        infile.close
    except IOError:
        print('An error occurred trying to read the file')
        print(filename)
main()
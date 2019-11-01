def main():
    filename = 'C:\\Users\\student\\Documents\\sales2.txt'
    sales_file = open(filename, 'r')

    line = sales_file.readline()

    while line != '':
        amount = float(line)
        print('{:.2f}'.format(amount))
        line = sales_file.readline()

    sales_file.close()

main()
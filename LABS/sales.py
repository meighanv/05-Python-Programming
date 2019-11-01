def main():
    num_days = int(input('For how many days do you have sales?\n'))
    filename = 'C:\\Users\\student\\Documents\\sales2.txt'
    sales_file = open(filename, 'w')

    for count in range(1, num_days + 1):
        sales = float(input('Enter sales for day # {}\n'.format(str(count))))
        sales_file.write(str(sales) + '\n')
    
    sales_file.close()
    print('Data written to {}'.format(filename))

main()
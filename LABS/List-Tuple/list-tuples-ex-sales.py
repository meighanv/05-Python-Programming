#Defining constant of days of the week
DAYS = ('MON','TUE','WED','THU','FRI','SAT','SUN')

#Define Main function
def main():
    sales = []
    getSales(sales,DAYS)
    measureSales(sales)

def getSales(salesArray,DAYS):
    for day in DAYS:
        sale = -1.0
        while sale == -1.0:
            #Testing user input via try/except
            try:
                sale = float(input(f'Provide the sales for {day}:'))
                salesArray.append(sale)
            except:
                print('A valid sale number was not provided')

def measureSales(salesArray):
    total = 0.0
    for sale in salesArray:
        total += sale
    print(f'Total sales for the week is ${total}')
    print('Average sales for the week is ${}'.format(total/len(salesArray)))

#Call main
main()
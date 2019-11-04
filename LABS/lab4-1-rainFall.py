#Constant array for Months
MONTHS = ('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC')

#Average rainfall
#Define main function
def main():
    #Array for rainfall numbers
    rainFall = []
    years = getYears()
    getRainfall(years, rainFall, MONTHS)
    measureRain(rainFall)


def getYears():
    #Initial prompt for input
    years = input('How many years of rainfall data to input?\n')
    #Input validation checking numeric and a positive number
    while int(years) <= 0 and years.isnumeric() == False:
        years = input('Invalid input. How man years of rainfall data to input?\n')
    return int(years)

def getRain(month,year):
    #Initial prompt for input
    rain = input('How much rain for {} in year {}?\n'.format(month,year))
    #Input validation checking numeric and a positive number
    while float(rain) < 0 and year.replace('.','').isnumeric() == False:
        rain = input('Invalid input. How much rain for {} in year {}?\n')
    return float(rain)

def getRainfall(years, rainFall, months):
    for i in range(years):
        for j in months:
            rainFall.append(getRain(j,i+1))

def measureRain(rainFall):
    total = 0
    for i in rainFall:
        total += i
    print('Total months of rainfall in data: {}'.format(len(rainFall)))
    print('Total rainfall: {:.2f} inches'.format(total))
    print('Average monthly rainfall: {:.2f}'.format(total/len(rainFall)))
    print('The maximum rainfall was {}'.format(max(rainFall)))
    print('The minimum rainfall was {}'.format(min(rainFall)))
    

main()
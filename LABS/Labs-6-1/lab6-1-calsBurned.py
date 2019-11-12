#Setting constant of treadmill Calories per minute 
CALS_PER_MIN = 3.9

#Define main function
def main():
    intervals = [10,15,20,25,30]
    calsBurned(intervals)

#Funtion to calculate calories burned for each interval
def calsBurned(time):
    for i in time:
        #Displaying the interval measured and the calculated calories burned
        print('Calories burned in {:d} minutes: {:.2f}'.format(i, float(i*CALS_PER_MIN)))

#Calling main
main()
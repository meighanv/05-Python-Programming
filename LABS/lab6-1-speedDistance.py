#Speed and Distance given time
#Define main function
def main():
    print('Your expected distance to cover is: {:.2f} miles'.format(calcDistance(getSpeed(),getTime())))

def getSpeed():
    speed = input('Provide the speed in MPH:\n')
    #Input validation checking numeric and a positive number
    while float(speed) <= 0 and speed.replace('.','').isnumeric() == False:
        speed = input('Invalid input. Provide the speed:\n')
    return float(speed)

def getTime():
    time = input('Provide the time in hours:\n')
    #Input validation checking numeric and a positive number
    while float(time) <= 0 and time.replace('.','').isnumeric() == False:
        time = input('Invalid input. Provide the time:\n')
    return float(time)

def calcDistance(s,t):
    return s * t
    

main()
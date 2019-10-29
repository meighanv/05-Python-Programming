#Declaring variable for speed calculation
speed = 0
time = [5, 8, 10]
distance = 0

#Getting user input for speed
speed = input('How fast in MPH are you traveling?\n')

#for loop to go through the time intervals
for i in time:
    print('If traveling at {} for {} hours, you will have traveled {} miles.\n'.format(speed,i,int(speed)*i))


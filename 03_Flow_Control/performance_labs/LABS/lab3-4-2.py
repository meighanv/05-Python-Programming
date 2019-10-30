
#Start main
def main():
    #Take user input for dimensions
    length = float(input('What is the length of your rectangle:\n'))
    width = float(input('What is the width of your rectangle:\n'))
    #Printing result using the calcArea function
    print('The area of your rectangle is {}'.format(calcArea(length,width)))

#Define the calcArea function
def calcArea(leng, wid):
    #Calculating the area
    return float(leng * wid)

main()
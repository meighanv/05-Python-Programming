#Defining CONSTANT array of primary colors
PRI_COLORS = ['red','blue','yellow']
MIXES = {'redblue': 'purple',
    'bluered': 'purple',
    'blueyellow': 'green',
    'yellowblue': 'green',
    'yellowred': 'orange',
    'redyellow': 'orange'
    }
def main():
    color1 = getColor()
    color2 = getColor()
    mixColor(color1,color2)

def getColor():
    print(PRI_COLORS)
    color = input('Please select a primary color from above list:\n')
    while color.lower() not in PRI_COLORS:
        color = input('Invalid selection. Please select a primary color from above list:\n')
    return color

def mixColor(c1,c2):
    if c1.lower() == c2.lower():
        print('Your resultant color is {}'.format(c1))
    else:
        newColor = c1+c2
        print('Your resultant color is {}'.format(MIXES[newColor]))

main()
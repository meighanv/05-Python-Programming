# GUI - Allows user to interact with OS using grapics
# In python we can use tkinter module to create simple GUIs
# There are other modules available but this ships with python
# There are WIDGETS
# ***********************
# Button - button that can cause an action when clicked
# Canvas - A rectangular area that can be used to display graphics
# Check button = a button that toggles 'on'/'off'
# Entry - An area that takes a single line of input from user
# Frame - A container that can hold other widgets
# Label - An area that displays one line of text or an image
# Listbox - A list from which the user may select an item
# Menu - A list of choices that are displayed when a user clicks 
#       the menu button widget
# Menubutton - A menu that is displayed on the screen and may be 
#       clicked bu the user
# Radiobutton - A widget that can be either selected or deselected
# Scale - Widget that allows the use to select a value by moving
#        a slider 
# Scrollbar - Can be used w/ some other types of widgets to provide
#           scrolling capability
# Text - A widget that allows the user to enter multiple lines of input
# TopLevel - a container, like a frame, but displayed in its own window 
# effbot.org/tkinterbook/text.html

"""
​
1. Name and Address
    Write a GUI program that displays your name and address when a button is clicked. 
    When the user clicks the Show Info button, the program should display your name and
    address. Mess with the display to make it look neat.
​
2. Latin Translator
    Look at the following list of Latin words and their meanings.
        Latin       English
        sinister    left
        dexter      right
        medium      center
    Write a GUI program that translates the Latin words to English. The window should have
    three buttons, one for each Latin word. When the user clicks a button, the program displays 
    the English translation in a label.
​
3. Miles Per Gallon Calculator
    Write a GUI program that calculates a car’s gas mileage. The program’s window should
    have Entry widgets that let the user enter the number of gallons of gas the car holds, and
    the number of miles it can be driven on a full tank. When a Calculate MPG button is
    clicked, the program should display the number of miles that the car may be driven per gallon of 
    gas. Use the following formula to calculate miles-per-gallon:
​
        MPG = miles/gallons
​
4. Celsius to Fahrenheit
    Write a GUI program that converts Celsius temperatures to Fahrenheit temperatures. The user
    should be able to enter a Celsius temperature, click a button, and then see the equivalent
    Fahrenheit temperature. Use the following formula to make the conversion:
​
        F = (9/5)C + 32
​
    F is the Fahrenheit temperature and C is the Celsius temperature.
​
5. Property Tax
    A county collects property taxes on the assessment value of property, which is 60 percent
    of the property’s actual value. If an acre of land is valued at $10,000, its assessment value
    is $6,000. The property tax is then $0.64 for each $100 of the assessment value. The tax
    for the acre assessed at $6,000 will be $38.40. Write a GUI program that displays the
    assessment value and property tax when a user enters the actual value of a property.
​
6. Joe’s Automotive
    Joe’s Automotive performs the following routine maintenance services:
        • Oil change          —   $26.00
        • Lube job            —   $18.00
        • Radiator flush      —   $30.00
        • Transmission flush  —   $80.00
        • Inspection          —   $15.00
        • Muffler replacement —   $100.00
        • Tire rotation       —   $20.00
    Write a GUI program with check buttons that allow the user to select any or all of these
    services. When the user clicks a button the total charges should be displayed.
​
"""
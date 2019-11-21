# The app will take in a name and randomly generate a greeting

import tkinter as tk
import random

window = tk.Tk()
window.title('Salutations')
window.geometry("400x400")


#Functions
def phraseGenerator():
    # Create a list of greetings for random selection
    phrases = ['Hello ', 'What\'s up ', 'Howdy ','Aloha ']
    name = str(entry1.get())
    return random.choice(phrases) + name
def phraseDisplay():
    # Get greeting from phrase generator
    greeting = phraseGenerator()
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0,row=3)

    greeting_display.insert(tk.END, greeting)
    return 


# Setting up a label

label1 = tk.Label(text = 'How you doin' )
label1.grid(column=0, row=0)

label2 = tk.Label(text = "what is your name?")
label2.grid(column=0, row=1)

# Entry
# No Args because we want user input
entry1 = tk.Entry() 
entry1.grid(column=1, row=1)

# Button
button1 = tk.Button(text = 'Click Me', command=phraseDisplay)
button1.grid(column=0, row=2)

window.mainloop()
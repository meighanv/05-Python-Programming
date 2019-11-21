import tkinter as tk
from tkinter import StringVar

def change():
    v.set("goodbye")
    #label.pack()

window = tk.Tk()

# Set the title for your window
window.title('Auto Shop')

# Set size of window
window.geometry("600x600")

# Adding a label
v = StringVar()
title = tk.Label(textvariable=v)
v.set('hello')
# grid() tells you where you want the label, (0,0) is default
title.pack() 

click = tk.Button(text = "Change", bg = "blue", command=change)
click.pack()

window.mainloop()

import tkinter as tk

# Instantiate tkinter object
window = tk.Tk()

# Set the title for your window
window.title('First TKinter App')

# Set size of window
window.geometry("400x400")

# Adding a label
title = tk.Label(text = "Hello World")

# grid() tells you where you want the label, (0,0) is default
title.grid()

# pack() this allows the module to force objects into the existing window
#title.pack()

# Adding a button
button1 = tk.Button(text = "Click Me", bg = "red")
button1.grid(column=0, row=1)

# Adding entry

entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

# Add text field
text_field = tk.Text(master = window, height = 10, width = 30)
text_field.grid(column=0, row=3)

# This opens window and keeps it open until closed
# Everything you do must be between this and instantiation
# This is always at the bottom
# Continueously puts window in a loop to keep open 
window.mainloop()
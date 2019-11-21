""" 6. Joe’s Automotive
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
​"""
import tkinter as tk
from autoservice import AutoService
from tkinter import ttk 

# Calc total from checkboxes in 'selected' state
def calcTotal(services, svc0, svc1, svc2, svc3, svc4, svc5, svc6 ):
    total = 0
    if 'selected' in svc0.state():
        total += services[0].getCost()
    else:
        total += 0
    if 'selected' in svc1.state():
        total += services[1].getCost()
    else:
        total += 0
    if 'selected' in svc2.state():
        total += services[2].getCost()
    else:
        total += 0
    if 'selected' in svc3.state():
        total += services[3].getCost()
    else:
        total += 0
    if 'selected' in svc4.state():
        total += services[4].getCost()
    else:
        total += 0
    if 'selected' in svc5.state():
        total += services[5].getCost()
    else:
        total += 0
    if 'selected' in svc6.state():
        total += services[6].getCost()
    else:
        total += 0
    return total

def dispTotal():
    total = calcTotal(services, svc0, svc1, svc2, svc3, svc4, svc5, svc6)
    totalString = 'Service Total: $'+str(total)
    stringVar.set(totalString)
    #label.pack()

# Setting services into list
services = []
services.append(AutoService('Oil change',26.00))
services.append(AutoService('Lub Job',18.00))
services.append(AutoService('Radiator Flush', 30.00))
services.append(AutoService('Transmission Flush', 80.00))
services.append(AutoService('Inspection', 15.00))
services.append(AutoService('Muffler Replacement', 100.00))
services.append(AutoService('Tire Rotation', 20.00))

window = tk.Tk()

# Set the title for your window
window.title('Auto Shop')

# Set size of window
window.geometry("600x600")

# Adding a label
title = tk.Label(text = "Welcome to the Auto Shop")

# grid() tells you where you want the label, (0,0) is default
title.pack() 

# Setting menu

# class svcCheck(ttk.Checkbutton):
#     def __init__(self, master, service, cost):
#         c = ttk.Checkbutton(master, text=service+'\t\t$'+str(cost))
#         c.pack()
        


svc0 = ttk.Checkbutton(window, text=services[0].getDesc()+'\t\t$'+str(services[0].getCost()))     
svc1 = ttk.Checkbutton(window, text=services[1].getDesc()+'\t\t$'+str(services[1].getCost()))    
svc2 = ttk.Checkbutton(window, text=services[2].getDesc()+'\t\t$'+str(services[2].getCost()))    
svc3 = ttk.Checkbutton(window, text=services[3].getDesc()+'\t\t$'+str(services[3].getCost()))    
svc4 = ttk.Checkbutton(window, text=services[4].getDesc()+'\t\t$'+str(services[4].getCost()))    
svc5 = ttk.Checkbutton(window, text=services[5].getDesc()+'\t\t$'+str(services[5].getCost())) 
svc6 = ttk.Checkbutton(window, text=services[6].getDesc()+'\t\t$'+str(services[6].getCost()))    
svc0.pack() 
svc1.pack()
svc2.pack()
svc3.pack()
svc4.pack()
svc5.pack()
svc6.pack()
total = calcTotal(services, svc0, svc1, svc2, svc3, svc4, svc5, svc6)
totalString = 'Service Total: $'+str(total)
stringVar = tk.StringVar()
stringVar.set(totalString)
screenTotal = tk.Label(window, textvariable=stringVar).pack()


clickCalc = tk.Button(text = "Calculate Total", bg = "blue", command=dispTotal)
clickCalc.pack()








window.mainloop()



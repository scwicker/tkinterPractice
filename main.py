#must include import tkinter to use GUI stuff
from tkinter import *

#create a tkinter object which will be outer shell window 
outerShell=Tk()

#labels put text into a tkinter window. First param is which window. second param text
labelVar = Label(root, text="This is too easy")

#this is where we can tell tkinter to position window
theLabel.pack()


#must loop or else screen will just flash window and disappear 
root.mainloop()

#must include import tkinter to use GUI stuff
from tkinter import *

#create a tkinter object which will be outer shell window 
outerShell=Tk()

#create two frames for now 
topFrame = Frame(outerShell)
topFrame.pack()
bottomFrame = Frame(outerShell)
bottomFrame.pack()

#add some buttons to the frames #when not in mac, can add button colors with 3rd param 
#first param is which frame, second is text
button1 = Button(topFrame, text="button 1")
button2 = Button(topFrame, text="button 2")
button3 = Button(bottomFrame, text="button 3")
button4 = Button(bottomFrame, text="button 4")

#labels put text into a tkinter window. First param is which window. second param text
labelVar = Label(outerShell, text="This is just some text in outerShell")

#this is where we can tell tkinter to position window
labelVar.pack()
button2.pack(side=LEFT)
button1.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


#must loop or else screen will just flash window and disappear 
outerShell.mainloop()

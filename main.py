#must include import tkinter to use GUI stuff
from tkinter import *

#create a tkinter object which will be outer shell window 
outerShell=Tk()


#------------------------------------------------------------------------------------------------------
# in this section we are going to use the grid system instead of just packing 

label_1 = Label(outerShell, text = "Enter first number")
label_2 = Label(outerShell, text = "Enter second number")
label_submit = Label(outerShell, text = "Click submit for results")
submit_button = Button(outerShell, text = "Submit")
label_results = Label(outerShell, text = "The product of your two numbers is:")

label_1.grid(row=0, column = 0)
label_2.grid(row=1, column = 0)
label_submit.grid(row=2, column = 0)
submit_button.grid(row=2, column =1)
label_results.grid(row=3, column = 0)

textinput1 = Entry(outerShell)
textinput2 = Entry(outerShell)
textinput1.grid(row = 0, column = 1)
textinput2.grid(row = 1, column = 1)

#------------------------------------------------------------------------------------------------------




#must loop or else screen will just flash window and disappear 
outerShell.mainloop()

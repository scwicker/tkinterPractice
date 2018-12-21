#must include import tkinter to use GUI stuff
from tkinter import *

#create a tkinter object which will be outer shell window 
outerShell=Tk()


#------------------------------------------------------------------------------------------------------
# in this section we are going to use the grid system instead of just packing 



def dothemath ():
	productResult = num1.get() * num2.get()
	print (productResult)
	productLabel = Label(outerShell, text = productResult)
	productLabel.grid(row=3, column=3)
	return productResult

def clearField(tInput):
	tInput.delete(0,END)

num1 = IntVar()
num2 = IntVar()

textinput1 = Entry(outerShell, textvariable=num1)
textinput2 = Entry(outerShell, textvariable=num2)
	

label_1 = Label(outerShell, text = "Enter first number")
label_2 = Label(outerShell, text = "Enter second number")
label_submit = Label(outerShell, text = "Click submit for results")
submit_button = Button(outerShell, text = "Submit", command=dothemath)
clear1_button = Button(outerShell, text = "Clear", command= lambda: clearField(textinput1))
clear2_button = Button(outerShell, text = "Clear", command= lambda: clearField(textinput2))
label_results = Label(outerShell, text = "The product of your two numbers is:")

label_1.grid(row=0, column = 0)
label_2.grid(row=1, column = 0)
label_submit.grid(row=2, column = 0)
submit_button.grid(row=2, column =1)
label_results.grid(row=3, column = 0)


textinput1.grid(row = 0, column = 1)
textinput2.grid(row = 1, column = 1)
clear1_button.grid(row = 0, column =2)
clear2_button.grid(row = 1, column =2)



	
	

#------------------------------------------------------------------------------------------------------




#must loop or else screen will just flash window and disappear 
outerShell.mainloop()

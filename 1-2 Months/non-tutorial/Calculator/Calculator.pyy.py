from tkinter import *

root = Tk()
root.title('Window')
root.geometry("312x500")
root.resizable(0, 0)
#x
# def on_click():
#
#
#
#
# def equals():
#
#
#
# def clear():

expression = " "
input_text = StringVar()

# Frame for the input. (Input field/Entry box, goes over the frame)
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground='black', highlightcolor='black', highlightthickness=1)
input_frame.pack(side=TOP, pady=2)

# Entry field for the input from the buttons
input_entry = Entry(input_frame, font=("Arial", 15, 'bold'),width=50, bg='#eee', bd = 0, justify = RIGHT )
input_entry.grid(row = 0, column = 0)
input_entry.pack(ipady=10)

# Frame for all the buttons below the input
button_frame = Frame(root, width = 312, height = 1000, bg = 'black')
button_frame.pack(side=BOTTOM)
button_frame2 = Frame(root, width = 312, height = 324, bg = 'black')
button_frame2.pack(side=LEFT)

# Clear Button
clear = Button(button_frame2, text = 'C', bd = 0, bg = "#eee", width = 25, height = 3)
clear.grid(row = 0, column = 0, columnspan = 3, pady = 1)

divide = Button(button_frame, text = "/", bd = 0, bg = "#eee", width = 8, height = 3)
divide.grid(row = 0, column = 3, padx = 1, pady = 1)

multiply = Button(button_frame, text = "*", bd = 0, bg = "#eee", width = 8, height = 3)
multiply.grid(row = 1, column = 3, padx = 1, pady =1)

subtract = Button(button_frame, text = "-", bd = 0, bg = "#eee", width = 8, height = 3)
subtract.grid(row = 2, column = 3, padx = 1, pady = 1)

addition = Button(button_frame, text = "+", bd = 0, bg = "#eee", width = 8, height = 3)
addition.grid(row = 3, column = 3, pady = 1)

equals = Button(button_frame, text = "=", bd = 0, bg = "#eee", width = 13, height = 3)
equals.grid(row = 3, column = 2, pady = 1)

zero = Button(button_frame, text = "0", bd = 0, bg = "#eee", width = 12, height = 3)
zero.grid(row = 3, column = 0, pady = 1)

# button_div = Button(button_frame, text = "/", bd = 0, bg = "#eee", width = 12, height = 3)
# button_div.grid(row = 0, column = 3, padx = 1, pady = 1)
# button_div = Button(button_frame, text = "/", bd = 0, bg = "#eee", width = 12, height = 3)
# button_div.grid(row = 0, column = 3, padx = 1, pady = 1)
# button_div = Button(button_frame, text = "/", bd = 0, bg = "#eee", width = 12, height = 3)
# button_div.grid(row = 0, column = 3, padx = 1, pady = 1)

root = mainloop()
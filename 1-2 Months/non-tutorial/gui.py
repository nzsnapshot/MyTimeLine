from tkinter import *

import tkinter.messagebox

from PIL import Image,ImageTk

window=Tk()
window.geometry("500x600")
window.title("Welcome")



#   Image

imge=Image.open("/Users/Snapshot/Desktop/pencil.png")
photo=ImageTk.PhotoImage(imge)

lab=Label(image=photo)
lab.pack()

#   Exit

def exit1():
    exit()

#   About

def abt():
    tkinter.messagebox.showinfo("Welcome to Snaps crib", "This is a raping with my ags")

#   Menu

menu=Menu(window)
window.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu = subm1)
subm1.add_command(label="Exit", command = exit)

subm2 = Menu(menu)
menu.add_cascade(label="Option", menu = subm2)
subm2.add_command(label="About", command = abt)









#   Variables

fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()
radio_var = StringVar()
var_c1 = IntVar()
var_c2 = IntVar()


def printt():
    first = fn.get()
    last = ln.get()
    dob1 = dob.get()
    country = var.get()
    python = "Python"
    Java = "Java"
    radio = radio_var.get()

    print(f"Your Full Name Is: {first} {last}")
    print(f"Your Date Of Birth is: {dob1}")
    print(f"You were born in: {country}")
    if var_c1.get() and var_c2.get():
        print(f"Your Favourite Languages are: {Java} , {python}")
    elif var_c1.get():
        print(f"Your Favourite Language is: {Java}")
    elif var_c2.get():
        print(f'Your Favourite Language is: {python}')
    else:
        print("Too bad you suck at everything ")
    print(f"And you're a: {radio}")



#   Title

label1=Label(window,text="Registration Form",relief="solid",width=20,font=("arial",19,"bold"))
label1.place(x=130,y=80)

#   First Name

label2=Label(window,text="First Name:",width=15,font=("arial",12,"bold"))
label2.place(x=105,y=140)

entry_1=Entry(window,textvar=fn)
entry_1.place(x=200,y=140)

#   Last Name

label3=Label(window,text="Last Name:",width=15,font=("arial",12,"bold"))
label3.place(x=105,y=190)

entry_2=Entry(window,textvar=ln)
entry_2.place(x=200,y=190)

#   Date of Birth

label4=Label(window,text="D.O.B:",width=15,font=("arial",12,"bold"))
label4.place(x=105,y=240)

entry_3=Entry(window,textvar=dob)
entry_3.place(x=200,y=240)

#   Country

label5=Label(window,text="Country:",width=15,font=("arial",12,"bold"))
label5.place(x=105,y=290)

list1=['India', 'New Zealand', 'America', 'Canada', 'Niggers']
droplist=OptionMenu(window,var,*list1)
var.set("select country")
droplist.config(width=18)
droplist.place(x=200,y=290)

#   Programming Language

label6=Label(window,text="Prog Lang:",width=15,font=("arial",12,"bold"))
label6.place(x=105,y=340)

cl = Checkbutton(window, text="Java", variable= var_c1, onvalue = 1, offvalue = 0)
cl.place(x=200,y=340)
cl2 = Checkbutton(window, text="Python", variable= var_c2, onvalue = 1, offvalue = 0)
cl2.place(x=260,y=340)


#   Gender

label7=Label(window,text="Gender",width=15,font=("arial",12,"bold"))
label7.place(x=105,y=390)

r1 = Radiobutton(window,text="Male",variable=radio_var,value="Male")
r1.place(x=200,y=390)
r2 = Radiobutton(window,text="Female",variable=radio_var,value="Female")
r2.place(x=260,y=390)

#   Sign up - button

b1=Button(window,text="Sign Up",width=12,fg="Green",bg="Red",command=printt)
b1.place(x=125,y=450)

#   Cancel - button

b2=Button(window,text="Cancel",width=12,fg="Green",bg="Red",command=exit1)
b2.place(x=250,y=450)

#   Login - Button

b3=Button(window,text="Login",width=12,fg="Red",bg="Red")
b3.place(x = 175,y = 485)





window.mainloop()

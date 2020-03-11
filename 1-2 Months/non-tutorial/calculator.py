from tkinter import *

window=Tk()
window.geometry("500x600")
window.title("Welcome")

num1 = float(input('Enter the First Number: '))
op = input('Enter the operator: ')
num2 = float(input('Enter the Second Number '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)


window.mainloop()
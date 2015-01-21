#! /usr/bin/python3

from tkinter import *
import pygame.mixer

def calc_add():
    num1 = int(add_num1.get())
    num2 = int(add_num2.get())
    add_disp.delete(0, END)
    add_disp.insert(0, str(num1 + num2))
    add_num1.delete(0, END)
    add_num2.delete(0, END)

def reset_add():
    add_num1.delete(0, END)
    add_num2.delete(0, END)

def calc_sub():
    num1 = int(sub_num1.get())
    num2 = int(sub_num2.get())
    sub_disp.delete(0, END)
    sub_disp.insert(0, str(num1 - num2))
    sub_num1.delete(0, END)
    sub_num2.delete(0, END)

def reset_sub():
    sub_num1.delete(0, END)
    sub_num2.delete(0, END)

def calc_mul():
    num1 = int(mul_num1.get())
    num2 = int(mul_num2.get())
    mul_disp.delete(0, END)
    mul_disp.insert(0, str(num1 * num2))
    mul_num1.delete(0, END)
    mul_num2.delete(0, END)

def reset_mul():
    mul_num1.delete(0, END)
    mul_num2.delete(0, END)

def calc_div():
    num1 = int(div_num1.get())
    num2 = int(div_num2.get())
    div_disp.delete(0, END)
    div_disp.insert(0, str(num1 / num2))
    div_num1.delete(0, END)
    div_num2.delete(0, END)

def reset_div():
    div_num1.delete(0, END)
    div_num2.delete(0, END)

    
app = Tk()
app.title("My calculator")

sounds = pygame.mixer
sounds.init()

Label(app, text="Addition:").pack()
add_num1 = Entry(app)
add_num1.pack(side = LEFT)
add_num2 = Entry(app)
add_num2.pack(side = LEFT)
add_disp = Entry(app)
add_disp.pack(side = LEFT)
Button(app, text="Add!",  command=calc_add).pack(side = LEFT)
Button(app, text="Reset", command=reset_add).pack(side = LEFT)

Label(app, text="Subtraction:").pack()
sub_num1 = Entry(app)
sub_num1.pack(side = LEFT)
sub_num2 = Entry(app)
sub_num2.pack(side = LEFT)
sub_disp = Entry(app)
sub_disp.pack(side = LEFT)
Button(app, text="Subtract!", command=calc_sub).pack(side = LEFT)
Button(app, text="Reset", command=reset_sub).pack(side = LEFT)

Label(app, text="Multiplication:").pack()
mul_num1 = Entry(app)
mul_num1.pack(side = LEFT)
mul_num2 = Entry(app)
mul_num2.pack(side = LEFT)
mul_disp = Entry(app)
mul_disp.pack(side = LEFT)
Button(app, text="Multiply!",  command=calc_mul).pack(side = LEFT)
Button(app, text="Reset", command=reset_mul).pack(side = LEFT)

Label(app, text="Division:").pack()
div_num1 = Entry(app)
div_num1.pack(side = LEFT)
div_num2 = Entry(app)
div_num2.pack(side = LEFT)
div_disp = Entry(app)
div_disp.pack(side = LEFT)
Button(app, text="Divide!",  command=calc_div).pack(side = LEFT)
Button(app, text="Reset", command=reset_div).pack(side = LEFT)

app.mainloop()

#! /usr/bin/python3

from tkinter import *
import pygame.mixer

class OperationPanel(Frame):
    def __init__(self, app, operation):
        Frame.__init__(self, app)
        if operation == "addition":
            Label(app, text="Addition:").pack()
            self.num1 = Entry(app)
            self.num1.pack(side = LEFT)
            self.num2 = Entry(app)
            self.num2.pack(side = LEFT)
            self.disp = Entry(app)
            self.disp.pack(side = LEFT)
            Button(app, text="Reset", command=self.reset_add).pack(side = RIGHT)
            Button(app, text="Add!",  command=self.calc_add).pack(side = RIGHT)
            
        elif operation == "subtraction":
            Label(app, text="Subtraction:").pack()
            self.num1 = Entry(app)
            self.num1.pack(side = LEFT)
            self.num2 = Entry(app)
            self.num2.pack(side = LEFT)
            self.disp = Entry(app)
            self.disp.pack(side = LEFT)
            Button(app, text="Reset", command=self.reset_sub).pack(side = RIGHT)
            Button(app, text="Subtract!", command=self.calc_sub).pack(side = RIGHT)
            
        elif operation == "multiplication":
            Label(app, text="Multiplication:").pack()
            self.num1 = Entry(app)
            self.num1.pack(side = LEFT)
            self.num2 = Entry(app)
            self.num2.pack(side = LEFT)
            self.disp = Entry(app)
            self.disp.pack(side = LEFT)
            Button(app, text="Reset", command=self.reset_mul).pack(side = RIGHT)
            Button(app, text="Multiply!",  command=self.calc_mul).pack(side = RIGHT)

        elif operation == "division":
            Label(app, text="Division:").pack()
            self.num1 = Entry(app)
            self.num1.pack(side = LEFT)
            self.num2 = Entry(app)
            self.num2.pack(side = LEFT)
            self.disp = Entry(app)
            self.disp.pack(side = LEFT)
            Button(app, text="Reset", command=self.reset_div).pack(side = RIGHT)
            Button(app, text="Divide!",  command=self.calc_div).pack(side = RIGHT)

           
    def calc_add(self):
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        self.disp.delete(0, END)
        self.disp.insert(0, str(num1 + num2))
        self.num1.delete(0, END)
        self.num2.delete(0, END)

    def reset_add(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)

    def calc_sub(self):
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        self.disp.delete(0, END)
        self.disp.insert(0, str(num1 - num2))
        self.num1.delete(0, END)
        self.num2.delete(0, END)

    def reset_sub(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)

    def calc_mul(self):
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        self.disp.delete(0, END)
        self.disp.insert(0, str(num1 * num2))
        self.num1.delete(0, END)
        self.num2.delete(0, END)

    def reset_mul(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)

    def calc_div(self):
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        self.disp.delete(0, END)
        self.disp.insert(0, str(num1 / num2))
        self.num1.delete(0, END)
        self.num2.delete(0, END)

    def reset_div(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)

    
app = Tk()
app.title("My calculator")

sounds = pygame.mixer
sounds.init()

OperationPanel(app, "addition").pack()
OperationPanel(app, "subtraction").pack()
OperationPanel(app, "multiplication").pack()
OperationPanel(app, "division").pack()

app.mainloop()

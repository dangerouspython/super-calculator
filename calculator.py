#! /usr/bin/python3

from tkinter import *
import pygame.mixer

class OperationPanel(Frame):
    def __init__(self, app, operation):
        Frame.__init__(self, app)
        if operation == "addition":
            self.oper = "add"
            Label(self, text="Addition:", fg="blue").pack()
            self.num1 = Entry(self)
            self.num1.pack(side = LEFT)
            self.num2 = Entry(self)
            self.num2.pack(side = LEFT)
            self.disp = Entry(self)
            self.disp.pack(side = LEFT)
            Button(self, text="Reset", command=self.reset).pack(side = RIGHT)
            Button(self, text="Add!",  command=self.calc).pack(side = RIGHT)
            
        elif operation == "subtraction":
            self.oper = "sub"
            Label(self, text="Subtraction:", fg="blue").pack()
            self.num1 = Entry(self)
            self.num1.pack(side = LEFT)
            self.num2 = Entry(self)
            self.num2.pack(side = LEFT)
            self.disp = Entry(self)
            self.disp.pack(side = LEFT)
            Button(self, text="Reset", command=self.reset).pack(side = RIGHT)
            Button(self, text="Subtract!", command=self.calc).pack(side = RIGHT)
            
        elif operation == "multiplication":
            self.oper = "mul"
            Label(self, text="Multiplication:", fg="blue").pack()
            self.num1 = Entry(self)
            self.num1.pack(side = LEFT)
            self.num2 = Entry(self)
            self.num2.pack(side = LEFT)
            self.disp = Entry(self)
            self.disp.pack(side = LEFT)
            Button(self, text="Reset", command=self.reset).pack(side = RIGHT)
            Button(self, text="Multiply!",  command=self.calc).pack(side = RIGHT)

        elif operation == "division":
            self.oper = "div"
            Label(self, text="Division:", fg="blue").pack()
            self.num1 = Entry(self)
            self.num1.pack(side = LEFT)
            self.num2 = Entry(self)
            self.num2.pack(side = LEFT)
            self.disp = Entry(self)
            self.disp.pack(side = LEFT)
            Button(self, text="Reset", command=self.reset).pack(side = RIGHT)
            Button(self, text="Divide!",  command=self.calc).pack(side = RIGHT)

           
    def calc(self):
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        self.disp.delete(0, END)

        if self.oper == "add":
            self.disp.insert(0, str(num1 + num2))
        elif self.oper == "sub":
            self.disp.insert(0, str(num1 - num2))
        elif self.oper == "mul":
            self.disp.insert(0, str(num1 * num2))
        elif self.oper == "div":
            self.disp.insert(0, str(num1 / num2))

    def reset(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)
        self.disp.delete(0, END)

    
app = Tk()
app.title("My calculator")

sounds = pygame.mixer
sounds.init()

OperationPanel(app, "addition").pack(fill=X)
OperationPanel(app, "subtraction").pack(fill=X)
OperationPanel(app, "multiplication").pack(fill=X)
OperationPanel(app, "division").pack(fill=X)

app.mainloop()

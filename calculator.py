#! /usr/bin/python3

from tkinter import *
import pygame.mixer

class OperationPanel(Frame):
    def __init__(self, app, operation):
        Frame.__init__(self, app)

        self.oper = operation[0:3]
        Label(self, text=operation, fg="#FFFFFF").pack()
        self.num1 = Entry(self)
        self.num1.pack(side = LEFT)
        self.num2 = Entry(self)
        self.num2.pack(side = LEFT)
        self.disp = Entry(self)
        self.disp.pack(side = LEFT)
        Button(self, text="Reset", command=self.reset).pack(side = RIGHT)
        Button(self, text=(operation + "!"),  command=self.calc).pack(side = RIGHT)
           
    def calc(self):
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        self.disp.delete(0, END)

        if self.oper == "Add":
            self.disp.insert(0, str(num1 + num2))
        elif self.oper == "Sub":
            self.disp.insert(0, str(num1 - num2))
        elif self.oper == "Mul":
            self.disp.insert(0, str(num1 * num2))
        elif self.oper == "Div":
            self.disp.insert(0, str(num1 / num2))

    def reset(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)
        self.disp.delete(0, END)

    
app = Tk()
app.title("My calculator")

sounds = pygame.mixer
sounds.init()

OperationPanel(app, "Addition").pack(fill=X)
OperationPanel(app, "Subtraction").pack(fill=X)
OperationPanel(app, "Multiplication").pack(fill=X)
OperationPanel(app, "Division").pack(fill=X)

app.mainloop()

#! /usr/bin/python3

from tkinter import *
import tkinter.messagebox
import pygame.mixer

class EmptyFrame(Frame):
    def __init__(self, app):
        Frame.__init__(self, app)

        Label(self, text='').pack()

class OpLabelFrame(Frame):
    def __init__(self, app, operation):
        Frame.__init__(self, app)

        Label(self, text=operation, fg="#FFFFFF",
              bg="#0066CC").pack(ipadx=5, ipady=3, side=LEFT)

class OperationPanel(Frame):
    def __init__(self, app, operation):
        Frame.__init__(self, app)

        EmptyFrame(app).pack(expand = True, fill = X)
        
        self.oper = operation[0:3]
        OpLabelFrame(app, operation).pack(side = TOP, expand = True, fill = X,
                                          padx = 4)
        
        self.num1 = Entry(self, width = 10, font = "Helvetica") 
        self.num1.pack(padx = 4, side = LEFT)
        
        if self.oper == "Add":
            text_="+"
        elif self.oper == "Sub":
            text_="-"
        elif self.oper == "Mul":
            text_="*"
        elif self.oper == "Div":
            text_="/"
            
        Label(self, text=text_, fg="Blue").pack(side = LEFT)
        
        self.num2 = Entry(self, width = 10, font = "Helvetica")
        self.num2.pack(side = LEFT, padx = 4)
        
        Label(self, text="=", fg="Blue").pack(side=LEFT)
        
        self.disp = Entry(self, width = 15, font = "Helvetica")
        self.disp.pack(side = LEFT, padx = 4)
        
        Button(self, text="Reset", command=self.reset,
               bg="#A00000", fg="#FFFFFF", relief="raised",
               font="Helvetica").pack(side = RIGHT)
        Button(self, text=(operation + "!"),  command=self.calc,
               font="Helvetica").pack(side = RIGHT)
           
    def calc(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
        except:
            tkinter.messagebox.showerror("Error!", "Entered values are not numbers.")
            return None

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

OperationPanel(app, "Addition").pack(fill=X, pady=5)
OperationPanel(app, "Subtraction").pack(fill=X, pady=10)
OperationPanel(app, "Multiplication").pack(fill=X, pady=10)
OperationPanel(app, "Division").pack(fill=X, pady=10)

app.mainloop()

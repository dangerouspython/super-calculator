#! /usr/bin/python3

from tkinter import *
import tkinter.messagebox
import pygame.mixer

class CalculatorFrame(Frame):
    def __init__(self, app):
        Frame.__init__(self, app)

        num1 = Entry(self, width = 10, font = "Helvetica", highlightcolor="#0066FF", fg = "#505050") 
        num1.pack(padx = 4, side = LEFT)

        num2 = Entry(self, width = 10, font = "Helvetica", highlightcolor="#0066FF", fg = "#505050")
        num2.pack(side = LEFT, padx = 4)

        disp_area = Entry(self, font = "Helvetica", highlightcolor="#0066FF", fg = "#505050")
        disp_area.pack(side = LEFT, fill = X, expand = False)
        
        ControlPanel(app, disp_area, num1, num2).pack(side = BOTTOM, fill = "both", expand = True)

class ControlPanel(Frame):
    def __init__(self, app, disp_area, num1, num2):
        Frame.__init__(self, app)

        self.disp = disp_area
        self.num1 = num1
        self.num2 = num2
        Button(self, text="Reset", command=self.reset,
               bg="#A00000", fg="#FFFFFF", relief="raised",
               font="Helvetica").pack()
        Button(self, text="Add!", command=self.calc,
               font="Helvetica").pack(side = LEFT)
        Button(self, text="Subtract!", command=self.calc,
               font="Helvetica").pack(side = LEFT)
        Button(self, text="Multiply!", command=self.calc,
               font="Helvetica").pack(side = LEFT)
        Button(self, text="Divide!", command=self.calc,
               font="Helvetica").pack(side = LEFT)
           
    def calc(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
        except:
            tkinter.messagebox.showerror("Error!", "Entered values are not numbers.")
            return None

        self.disp.delete(0, END)
        self.disp.insert(0, str(num1 + num2))

    def reset(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)
        self.disp.delete(0, END)

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
        
        
        if self.oper == "Add":
            text_="+"
        elif self.oper == "Sub":
            text_="-"
        elif self.oper == "Mul":
            text_="*"
        elif self.oper == "Div":
            text_="/"
            
        Label(self, text=text_, fg="Blue").pack(side = LEFT)
        
        Label(self, text="=", fg="Blue").pack(side=LEFT)
        
        self.disp = Entry(self, width = 15, font = "Helvetica",
                          highlightcolor="#0066FF", fg = "#505050")
        self.disp.pack(side = LEFT, padx = 4)
        
        

    
app = Tk()
app.title("My calculator")

sounds = pygame.mixer
sounds.init()

CalculatorFrame(app).pack(side = TOP, fill = "both", expand = True)

app.mainloop()

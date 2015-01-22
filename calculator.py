#! /usr/bin/python3

from tkinter import *
import tkinter.messagebox
import pygame.mixer
import math

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
               bg="#A00000", fg="#FFFFFF", font="Helvetica").pack()
        Button(self, text="Add!", command=lambda m="add":self.calc("add"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="Subtract!", command=lambda m="sub":self.calc("sub"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="Multiply!", command=lambda m="mul":self.calc("mul"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="Divide!", command=lambda m="div":self.calc("div"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="cos", command=lambda m="cos":self.calc("cos"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="sin", command=lambda m="sin":self.calc("sin"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="tan", command=lambda m="tan":self.calc("tan"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="cot", command=lambda m="cot":self.calc("cot"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="cosec", command=lambda m="cosec":self.calc("cosec"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="sec", command=lambda m="sec":self.calc("sec"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="arccos", command=lambda m="acos":self.calc("acos"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="arcsin", command=lambda m="asin":self.calc("asin"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="arctan", command=lambda m="atan":self.calc("atan"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="cosh", command=lambda m="cosh":self.calc("cosh"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="sinh", command=lambda m="sinh":self.calc("sinh"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="tanh", command=lambda m="tanh":self.calc("tanh"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="acosh", command=lambda m="acosh":self.calc("acosh"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="asinh", command=lambda m="asinh":self.calc("asinh"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="atanh", command=lambda m="atanh":self.calc("atanh"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="log", command=lambda m="log":self.calc("log"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="ln", command=lambda m="ln":self.calc("ln"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="pow", command=lambda m="pow":self.calc("pow"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="sqrt", command=lambda m="sqrt":self.calc("sqrt"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="exp", command=lambda m="exp":self.calc("exp"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="degrees", command=lambda m="degrees":self.calc("degrees"),
               font="Helvetica").pack(side = LEFT)
        Button(self, text="radians", command=lambda m="radians":self.calc("radians"),
               font="Helvetica").pack(side = LEFT)
           
    def calc(self, oper):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
        except:
            tkinter.messagebox.showerror("Error!", "Entered values are not numbers.")
            return None

        self.disp.delete(0, END)

        if oper == "add":
            self.disp.insert(0, str(num1 + num2))
        elif oper == "sub":
            self.disp.insert(0, str(num1 - num2))
        elif oper == "mul":
            self.disp.insert(0, str(num1 * num2))
        elif oper == "div":
            self.disp.insert(0, str(num1 / num2))
        elif oper == "cos":
            self.disp.insert(0, str(math.cos(num1)))
        elif oper == "sin":
            self.disp.insert(0, str(math.sin(num1)))
        elif oper == "tan":
            self.disp.insert(0, str(math.tan(num1)))
        elif oper == "cot":
            self.disp.insert(0, str(1/math.tan(num1)))
        elif oper == "cosec":
            self.disp.insert(0, str(1/math.sin(num1)))
        elif oper == "sec":
            self.disp.insert(0, str(1/math.cos(num1)))
        elif oper == "acos":
            self.disp.insert(0, str(math.acos(num1)))
        elif oper == "asin":
            self.disp.insert(0, str(math.asin(num1)))
        elif oper == "atan":
            self.disp.insert(0, str(math.atan(num1)))
        elif oper == "cosh":
            self.disp.insert(0, str(math.cosh(num1)))
        elif oper == "sinh":
            self.disp.insert(0, str(math.sinh(num1)))
        elif oper == "tanh":
            self.disp.insert(0, str(math.tanh(num1)))
        elif oper == "acosh":
            self.disp.insert(0, str(math.acosh(num1)))
        elif oper == "asinh":
            self.disp.insert(0, str(math.asinh(num1)))
        elif oper == "atanh":
            self.disp.insert(0, str(math.atanh(num1)))
        elif oper == "log":
            self.disp.insert(0, str(math.log(num1, num2)))
        elif oper == "ln":
            self.disp.insert(0, str(math.log(num1, math.e)))
        elif oper == "pow":
            self.disp.insert(0, str(math.pow(num1, num2)))
        elif oper == "sqrt":
            self.disp.insert(0, str(math.sqrt(num1)))
        elif oper == "exp":
            self.disp.insert(0, str(math.exp(num1)))
        elif oper == "degrees":
            self.disp.insert(0, str(math.degrees(num1)))
        elif oper == "radians":
            self.disp.insert(0, str(math.radians(num1)))
                             
    def reset(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)
        self.disp.delete(0, END)
    
app = Tk()
app.title("My calculator")

sounds = pygame.mixer
sounds.init()

CalculatorFrame(app).pack(side = TOP, fill = "both", expand = True)

app.mainloop()

from turtle import*
from tkinter import*

class Ventana(Frame):
    def __init__(self, master = None):
        r = Tk()
        r.title('Graficazos') 
        self.c = Canvas(master = r, width = 500, height = 630)
        self.c.pack()
    def pintar(self):
        t = RawTurtle(self.c)
        t.penup()
        t.goto(-250, 165)
        t.pendown()
        
        #Zona 1
        t.fillcolor("green")
        t.pencolor('green')
        t.begin_fill()
        t.goto(250, 165)
        t.goto(250, 315)
        t.goto(-250, 315)
        t.goto(-250, 165)
        t.end_fill()
        
        #Zona 2
        t.fillcolor("orange")
        t.pencolor('orange')
        t.begin_fill()
        t.goto(-250, -315)
        t.goto(-149, -315)
        t.goto(-149, 165)
        t.goto(-250, 165)
        t.end_fill()
        
        #Zona 3
        t.fillcolor("blue")
        t.penup()
        t.goto(-59,165)
        t.pendown()
        t.pencolor('blue')
        t.begin_fill()
        t.goto(-59, -315)
        t.goto(250, -315)
        t.goto(250, 165)
        t.goto(-59, 165)
        t.end_fill()
        
        #Zona 4
        t.fillcolor("purple")
        t.penup()
        t.goto(-59,-315)
        t.pendown()
        t.pencolor('purple')
        t.begin_fill()
        t.goto(-59, -95)
        t.goto(-149, -95)
        t.goto(-149, -315)
        t.goto(-59, -315)
        t.end_fill()
        
        self.c.mainloop()

ventana = Ventana() #Ventana digievolucionada
ventana.pintar()


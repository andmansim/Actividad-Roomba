from turtle import*
from tkinter import*

class Ventana(Frame):
    def __init__(self, master = None):
        r = Tk()
        r.title('Graficazos') 
        self.c = Canvas(master = r, width = 500, height = 630)
        self.c.pack()
        self.t = RawTurtle(self.c)
    def zona(self, color, x, y, x1, y1):
        
        self.t.fillcolor(color)
        self.t.pencolor(color)
        self.t.begin_fill()
        self.t.goto(x, y)
        self.t.goto(x, y1)
        self.t.goto(x1, y1)
        self.t.goto(x1, y)
        self.t.end_fill()
        
    def cambiar(self, x, y):
        
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
       
        
ventana = Ventana() #Ventana digievolucionada
ventana.cambiar(-250,165)
ventana.zona('pink', 250, 165, -250, 315)
ventana.cambiar(-250,-315)
ventana.zona('light green', -149, -315, -250, 165)
ventana.cambiar(-59,-315)
ventana.zona('light blue', 250, -315, -59, 165)
ventana.cambiar(-149,-315)
ventana.zona('violet', -149, -95, -59, -315)

ventana.mainloop()


'''
        self.t.fillcolor("pink")
        self.t.pencolor('pink')
        self.t.begin_fill()
        self.t.goto(250, 165)
        self.t.goto(250, 315)
        self.t.goto(-250, 315)
        self.t.goto(-250, 165)
        self.t.end_fill()
        
        #Zona 2
        t.fillcolor("light green")
        t.pencolor('light green')
        t.begin_fill()
        t.goto(-250, -315)
        t.goto(-149, -315)
        t.goto(-149, 165)
        t.goto(-250, 165)
        t.end_fill()
        
        #Zona 3
        t.fillcolor("light blue")
        t.penup()
        t.goto(-59,165)
        t.pendown()
        t.pencolor('light blue')
        t.begin_fill()
        t.goto(-59, -315)
        t.goto(250, -315)
        t.goto(250, 165)
        t.goto(-59, 165)
        t.end_fill()
        
        #Zona 4
        t.fillcolor("violet")
        t.penup()
        t.goto(-59,-315)
        t.pendown()
        t.pencolor('violet')
        t.begin_fill()
        t.goto(-59, -95)
        t.goto(-149, -95)
        t.goto(-149, -315)
        t.goto(-59, -315)
        t.end_fill()
        
        self.c.mainloop()
        '''
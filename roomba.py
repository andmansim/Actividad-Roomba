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
    def acabar(self):
        self.c.mainloop()
        
ventana = Ventana() #Ventana digievolucionada
ventana.cambiar(-250,165)
ventana.zona('pink', 250, 165, -250, 315)
ventana.cambiar(-250,-315)
ventana.zona('light green', -149, -315, -250, 165)
ventana.cambiar(-59,-315)
ventana.zona('light blue', 250, -315, -59, 165)
ventana.cambiar(-149,-315)
ventana.zona('violet', -149, -315, -59, -95)
ventana.acabar()


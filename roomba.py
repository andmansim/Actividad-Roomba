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
        t.pencolor('white')
        t.goto(-250, 165)
        
        #Zona 1
        t.fillcolor("green")
        t.pencolor('green')
        t.begin_fill()
        t.goto(250, 165)
        t.goto(250, 315)
        t.goto(-250, 315)
        t.goto(-250, 165)
        t.end_fill()
        
        self.c.mainloop()

ventana = Ventana() #Ventana digievolucionada
ventana.pintar()


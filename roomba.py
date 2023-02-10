from turtle import*
from tkinter import*

class Ventana(Frame):
    def __init__(self, master = None):
        #super(Ventana, self).__init__(master, width = 500, height = 630) #Indicamos el tamaño
        r = Tk()
        r.title('Graficazos') #Le ponemos nombre a nuestra ventana
        self.c = Canvas(master = r, width = 500, height = 630)
        self.c.pack()
    def pintar(self):
        t = RawTurtle(self.c)
        t.pencolor('green')
        t.forward(50)
        self.c.mainloop()

ventana = Ventana() #Ventana digievolucionada
ventana.pintar()



'''

r = Tk()
r.title('P')
c = Canvas(master = r, width = 500, height = 630)
c.pack()
t = RawTurtle(c)
t.pencolor('green')
t.forward(50)
c.mainloop()


'''



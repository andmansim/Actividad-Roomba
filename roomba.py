from turtle import*
import tkinter as tk

class Ventana(Frame):
    def __init__(self, master = None):
        super(Ventana, self).__init__(master, width = 500, height = 630) #Indicamos el tamaño
        self.master.title('Graficazos') #Le ponemos nombre a nuestra ventana
        self.pack()

ventana = Ventana() #Ventana digievolucionada
t = RawTurtle(ventana)
t.pencolor('green')
t.forward(50)
ventana.mainloop()






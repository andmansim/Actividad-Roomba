from tkinter import Frame

'''ventana = Frame()
ventana.mainloop() '''#Con esto crea una ventana y la deja abierta con el bucle

class Ventana(Frame):
    def __init__(self, master = None):
        super(Ventana, self).__init__(master, width = 320, height = 240) #Indicamos el tamaño
        self.master.title('Graficazos') #Le ponemos nombre a nuestra ventana
        self.pack()

ventana = Ventana() #Ventana digievolucionada
ventana.mainloop()
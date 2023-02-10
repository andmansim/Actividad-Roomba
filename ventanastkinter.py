from tkinter import Frame, Label, Scale
from tkinter import LEFT, HORIZONTAL

#VENTANA CON TKINTER

'''ventana = Frame()
ventana.mainloop() '''#Con esto crea una ventana y la deja abierta con el bucle

'''class Ventana(Frame):
    def __init__(self, master = None):
        super(Ventana, self).__init__(master, width = 320, height = 240) #Indicamos el tamaño
        self.master.title('Graficazos') #Le ponemos nombre a nuestra ventana
        self.pack()

ventana = Ventana() #Ventana digievolucionada
ventana.mainloop()'''

class Ventana(Frame):
    def __init__(self, master = None):
        super(Ventana, self).__init__(master, width = 320, height = 240) #Indicamos el tamaño
        self.master.title('Conversor C <-> F') #Le ponemos nombre a nuestra ventana
        self.pack()
        
    def initWidgets(self): #Creamos dos barritas, F y C que se mueven en escalas distintas
        self.FTexto = Label(self, text = 'F')
        self.FCursor = Scale(self, orient = HORIZONTAL, from_ = -148, to = 212, command= self.convertirFEnC) #añadimos el command después
        self.CTexto = Label(self, text = 'C')
        self.CCursor = Scale(self, orient = HORIZONTAL, from_ = -100, to = 100, command= self.convertirCEnF)
        for widget in [self.CTexto, self.CCursor, self.FTexto, self.FCursor]:
            widget.pack(side=LEFT)
           
    #Estas dos funciones sirven para que al mover uno de los dos cursores, el otro se mueva simultáneamente        
    def convertirCEnF(self, valor):
        C = float(valor)
        F = C * 9/5 + 32
        self.FCursor.set(F)
        
    def convertirFEnC(self, valor):
        F = float(valor)
        C = (F-32)*5/9 
        self.CCursor.set(C)
    
ventanuca = Ventana()
ventanuca.initWidgets()
ventanuca.mainloop() 


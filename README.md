# Actividad-Roomba

La pareja está formada por Ana López y Andrea Manuel. 
Hemos realizado una actividad del roomba y los ejercicios resueltos de la teoría, con comentarios demostrando nuestro entendimiento de cada proceso.

La dirección de github de este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Actividad-Roomba.git)

https://github.com/andmansim/Actividad-Roomba.git

Nuestro código es el siguiente:
# Coches
```
import time
import threading #Esto lo añadimos en la segunda parte
'''class Coche:
    def rodar(self):
        print('Avanza el coche')
        for i in range(10):#Hace que el coche avance 10 veces con un segundo de separación
            print('.')
            time.sleep(1)
            
    def girar(self):
        print('Giramos a la derecha') #Esto lo hacemos durante un segundo
        time.sleep(1)#Esperamos un seg
        
audi = Coche()
while True:
    audi.rodar()
    #Primero avanza y después gira, no puede hacer los dos movimientos simultaneamente
    audi.girar()
'''
#Hacemos programacion concurrente para resolver este problema

class Rodar(threading.Thread):
    def __init__(self) :
        super().__init__()
    def run(self):
        bloqueo1.acquire() #Esto es para marcar prioridades entre hilos y que no de error
        for i in range(5): #Avanzamos 5 y en intervalos de 1 segundo
            print('.')
            time.sleep(1)
            print('A la espera del bloqueo 2')
        bloqueo2.acquire()
        print('Bloqueo 2')
        bloqueo2.release() #quitamos el bloqueo 2
        bloqueo1.release() #quitamos el bloqueo 1 y ya pasa a lo siguiente
        
        
        
class Girar(threading.Thread):
    def __init__(self) :
        super().__init__()
    def run(self): #El run es una palabra clave
        bloqueo2.acquire()
        for i in range(3): #Giramos 3 pasos en intervalos de 1 segundo
            print('->')
            time.sleep(1)
            print('A la espera del bloqueo 1')
        bloqueo1.acquire()
        print('Bloqueo 1')
        bloqueo1.release()
        bloqueo2.release()
class Coche():
    def __init__(self):
        self.rodar = Rodar()
        self.girar=Girar()
    
    def run(self):
        self.rodar.start() #El método start del threat llama a los dos avanzar de cada clase y se ejecutan a la vez.
        self.girar.start()

bloqueo1 = threading.Lock()
bloqueo2 = threading.Lock()
mercedes = Coche()
mercedes.run()
```
# Qt
```
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QSpinBox, QLineEdit, QHBoxLayout, QComboBox

#VENTANA CON QT

class MainWindow(QMainWindow): 
    def __init__(self): 
        super(MainWindow, self).__init__() 

        widget = QWidget() #Este será el widget principal
        self.setCentralWidget(widget) #Lo ponemos como el principal
        diseño = QHBoxLayout() #Con esto nos sale la operacion en vertical
        widget.setLayout(diseño)

        #Con esto hacemos las casillas de las operaciones
        self.operando1 = QSpinBox () 
        self.operando2 = QSpinBox () 
        self.operacion = QComboBox ()
        [self.operacion.addItem(op) for op in ["+", "-", "*", "/"]] 
        self.resultado = QLineEdit() 
        widgets = [self.operando1, self.operacion, self.operando2, QLabel("="), self.resultado] 
        [diseño.addWidget(widget) for widget in widgets] 

        #Estas dos lineas son para que se envíe la señal de que se han cambiado los numeros de la operacion
        self.operando1.valueChanged.connect(self.calcular) 
        self.operando2.valueChanged.connect(self.calcular)
        self.operacion.currentIndexChanged.connect(self.calcular) #Con currentIndexChanged, cambiamos el resultado cuando se cambian los operandos

        self.calcular() #Lo ponemos aquí para que el valor se vaya actualizando siempre que se cambie un operando en la ventana (funcion calcular más adelante)

    def calcular(self): 
        a = self.operando1.value()
        b = self.operando2.value() 
 
        #Ponemos todas las opciones de operación y devolvemos el resultado correspondiente
        if (self.operacion.currentText() == "+"): 
            resultado = str(a + b) 
        elif (self.operacion.currentText() == "-"): 
            resultado = str(a - b) 
        elif (self.operacion.currentText() == "*"): 
            resultado = str(a * b) 
        elif (self.operacion.currentText() == "/"): 
            # Cogemos la excepción para que no pete con la división entre 0
            try: 
                resultado = str(a / b) 
            except ZeroDivisionError as e: 
                resultado = "División por cero" 
        # Cambiamos el campo texto con el resultado de la operación. 
        self.resultado.setText(resultado) 

app = QApplication(sys.argv) 
window = MainWindow() 
window.show()
sys.exit(app.exec_())
```
# Tkinter
```
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
```

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
![capcoches](/imagenes/capcoches.png)
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
![Ventanuca](Ventanuca.png)

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
![capventanas](/imagenes/cap_ventanasTkinter.png)

# Roomba
```
from turtle import*
from tkinter import*

#Representación de la habitación

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
        
ventana = Ventana() 
ventana.cambiar(-250,165)
ventana.zona('pink', 250, 165, -250, 315)
ventana.cambiar(-250,-315)
ventana.zona('light green', -149, -315, -250, 165)
ventana.cambiar(-59,-315)
ventana.zona('light blue', 250, -315, -59, 165)
ventana.cambiar(-149,-315)
ventana.zona('violet', -149, -315, -59, -95)
ventana.acabar()

#Cálculo del área

def calculoarea(b, h): #b: base, h: altura
    area = b * h #Esto nos lo da en cm2, lo pasamos a m2
    area = area/100
    return area

def calculotiempo(a, v): #a: area, v: velocidad
    tiempo = a/v #Nos da el tiempo en segundos, lo pasamos a minutos
    tiempo = tiempo/60
    return tiempo

print('El roomba va a una velocidad de 0.5m2/s')
vel = 0.5#m2/s
area1 = calculoarea(500, 150)
tiempo1 = calculotiempo(area1, vel)
area2 = calculoarea(101, 480)
tiempo2 = calculotiempo(area2, vel)
area3 = calculoarea(309, 480)
tiempo3 = calculotiempo(area3, vel)
area4 = calculoarea(90, 220)
tiempo4 = calculotiempo(area4, vel)
print('El tiempo que tarda en limpiar cada zona es de: ')
print(tiempo1, tiempo2, tiempo3, tiempo4)
tiempoT = tiempo3 + tiempo1 + tiempo2 + tiempo4
print('El tiempo total que tarda en limpiar la habitacion es: ' + str(tiempoT) + 'min')
print('Es decir, ' + str(tiempoT/60) + 'h')
```
![caproomba](/imagenes/caproomba.png)
![caproomba2](/imagenes/caproomba2.png)

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
        for i in range(5): #Avanzamos 5 y en intervalos de 1 segundo
            print('.')
            time.sleep(1)

class Girar(threading.Thread):
    def __init__(self) :
        super().__init__()
    def run(self): #El run es una palabra clave
        for i in range(3): #Giramos 3 pasos en intervalos de 1 segundo
            print('->')
            time.sleep(1)

class Coche():
    def __init__(self):
        self.rodar = Rodar()
        self.girar=Girar()
    
    def run(self):
        self.rodar.start() #El método start del threat llama a los dos avanzar de cada clase y se ejecutan a la vez.
        self.girar.start()

mercedes = Coche()
mercedes.run()
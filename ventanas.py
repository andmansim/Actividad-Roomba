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


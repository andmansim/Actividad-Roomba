import time
class Coche:
    def rodar(self):
        print('Avanza el coche')
        for i in range(10):#Hace que el coche avance 10 veces con un segundo de separación
            time.sleep(1)
            
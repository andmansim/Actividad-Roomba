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
from turtle import*
import tkinter as tk

r = tk.Tk()
r.title('Patata')
ventana = tk.Canvas(master=r, width=500, height=500)
ventana.pack()

t = RawTurtle(ventana)
t.pencolor('green')
t.forward(50)

r.mainloop()


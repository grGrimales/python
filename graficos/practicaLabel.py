from tkinter import* 

root=Tk() #creacion de la raiz

miFrame=Frame(root, width=500, height=400) #con esto le indicamos que va dentro de la raiz con ancho y alto

miFrame.pack() #con esto lo empaquetamos

miImagen= PhotoImage(file="Luz.png")
miLabel= Label(miFrame, image=miImagen)

#miLabel= Label(miFrame, text="Hola alumnos de python", fg="green", font=("Comic Sans MS", 18))
#con esto introducimos texto en el frame
miLabel.place(x=100, y=200)
#esto es para indicar la posicion del texto en el frame
#se puede abreviar si mas adelante no vamos a modificar el Label:
#Label(miFrame, text="Hola alumnos de python").place(x=100, y=200)


root.mainloop()
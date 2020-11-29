from tkinter import*

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)

miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1,padx=10, pady=10)
#con la funcion grid agregamos una tabla donde row es fila y se cuenta desde 0
#padx=  con esta funcion cambiamos la separacion horizontal desde el contenedor padre hasta el siguiente lemento
# pady=10 con esta cambiamos la sepacion vertical
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1,padx=10, pady=10)
cuadroApellido.config(fg="green", justify="center")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=10)

cuadroContrasena=Entry(miFrame)
cuadroContrasena.grid(row=3, column=1, padx=10, pady=10)
cuadroContrasena.config(show="*")

nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=0, column=0, sticky="w",padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido")
apellidoLabel.grid(row=1, column=0,sticky="w",padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion")
direccionLabel.grid(row=2, column=0, sticky="e",padx=10, pady=10)
#con la funcion sticky logramos colocar el texto en la tabla en la posicion que deseamos con los puntos
#cardinales

contrasenaLabel=Label(miFrame, text="Contraseña")
contrasenaLabel.grid(row=3, column=0, sticky="e",padx=10, pady=10)

raiz.mainloop()
from tkinter import*

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)

miFrame.pack()
minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
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

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)


scrollVert=Scrollbar(miFrame, command=textoComentario.yview) #con esto agregamos la barra vertical
scrollVert.grid(row=4, column=2, sticky="nsew")
#con la funcion sticky="nsew" logramos que se coloque del largo del texto
textoComentario.config(yscrollcommand=scrollVert.set) #con esto logramos que la el posicionador se coloque en la posicion donde vamos escribiendo



nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=0, column=0, sticky="w",padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido")
apellidoLabel.grid(row=1, column=0,sticky="w",padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion")
direccionLabel.grid(row=2, column=0, sticky="w",padx=10, pady=10)
#con la funcion sticky logramos colocar el texto en la tabla en la posicion que deseamos con los puntos
#cardinales

contrasenaLabel=Label(miFrame, text="Contraseña")
contrasenaLabel.grid(row=3, column=0, sticky="w",padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="w",padx=10, pady=10)

def codigoBoton():
	minombre.set("Grediana")

botonEnvio=Button(raiz, text="enviar", command=codigoBoton) #con command y la funcion codigoBoton logramos que el boton envie informacion
botonEnvio.pack()
raiz.mainloop()
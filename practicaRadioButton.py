from tkinter import*

root=Tk()

varOpcion=IntVar()
#esta es la variable que debemos crear para un Radiobutton

def imprimir():
	#print(varOpcion.get())
	if varOpcion.get()==1:
		etiqueta.config(text="Has elegido Masculino")
	else:
		etiqueta.config(text="Has elegido Femenino")
Label(root, text="Genero: ").pack()

Radiobutton(root, text="Masculino", variable=varOpcion,value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOpcion,value=2,command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()
root.mainloop()

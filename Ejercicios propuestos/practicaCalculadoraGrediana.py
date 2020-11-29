from tkinter import*

raiz=Tk ()
raiz.title("Calculadora")
raiz.geometry("145x200")
miFrame=Frame (raiz)

miFrame.pack()
operacion=""
resultado=0
miFrame.config(background="#8B9C99")

#------------PANTALLA----------------
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="#43F1F3", fg="blue", justify="right")

#--------------pulsaciones teclado-----------
def numeroPulsado(num):
	global operacion


	if operacion!="":
		numeroPantalla.set(num)
		operacion=""
	else:

		numeroPantalla.set(numeroPantalla.get()+ num)  #el metodo get lo que hace es que mira lo que hay en pantalla y agregamo el valor que estemos indicando


#-----------------------BORRAR----------------------------------

def borra():
    borrado = numeroPantalla.get()
    numeroPantalla.set(borrado[0:-1])
#-------------Funcion suma-----------------------------------
def digito(num):

    global boton

    boton = boton + str(num)

    calculo.set(boton)

def igual():

    try:

        global boton

        total = str(eval(boton))

        calculo.set(total)

        boton = ""

    except:

        calculo.set(" error ")

def limpiar():

    calculo.set("")
def digito(num):

    global boton

    boton = boton + str(num)

    calculo.set(boton)

def igual():

    try:

        global boton

        total = str(eval(boton))

        calculo.set(total)

        boton = ""

    except:

        calculo.set(" error ")

def limpiar():

    calculo.set("")
def suma(num):
	global operacion
	global resultado

	resultado+= int(num)

	operacion="suma"
	reset_pantalla=True
	numeroPantalla.set(resultado)
#-----------------Funcion resta----------------------------------------------


#-------------------FUNCION EL_RESULTADO----------------------------

def el_resultado():
 	global resultado

 	numeroPantalla.set(resultado+int(numeroPantalla.get()))

 	resultado=0


#-----------FILA 1----------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton7.config(background="blue")

boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton8.config(background="blue")

boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
boton9.config(background="blue")

botonDiv=Button(miFrame, text="/", width=3 )
botonDiv.grid(row=2, column=4)
botonDiv.config(background="blue")


#-----------FILA 2----------------
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton4.config(background="blue")


boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton5.config(background="blue")

boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
boton6.config(background="blue")

botonMul=Button(miFrame, text="x", width=3)
botonMul.grid(row=3, column=4)
botonMul.config(background="blue")

#-----------FILA 3----------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton1.config(background="blue")

boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton2.config(background="blue")

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
boton3.config(background="blue")

botonRest=Button(miFrame, text="-", width=3, command=lambda:digito())
botonRest.grid(row=4, column=4)

botonRest.config(background="blue")
#-----------FILA 4----------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
boton0.config(background="blue")

botoncoma=Button(miFrame, text=",", width=3)
botoncoma.grid(row=5, column=2)
botoncoma.config(background="blue")

botonIgual=Button(miFrame, text="=", width=3, command=lambda: el_resultado())
botonIgual.grid(row=5, column=3)
botonIgual.config(background="blue")

botonSuma=Button(miFrame, text="+", width=3,command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)
botonSuma.config(background="blue")

#--------------fila 5----------------

botonBorrar=Button(miFrame, text="borrar", width=3,command=lambda:borra())
botonBorrar.grid(row=6, column=2,columnspan=2,pady=15)
botonBorrar.config(background="blue",pady=10)






raiz.mainloop()
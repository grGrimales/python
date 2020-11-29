#la funcion decoradora añade funcionalidad a otra funcion se construye de la siguiente forma:
def funcion_decoradora(funcion_parametro):

	def funcion_interior(*args,**kwargs): #con *args le indicamos que puede recibir varios argumentosel nombre se usa por convencion puede ir cualquier otro
#en esta funcion va las acciones que decoren a las funciones que queremos 
		print("Vamos a realizar un calculo:")

		funcion_parametro(*args,**kwargs)# *kwarg este nombre se usa por convencion puedeir cualquier otro
		#su nombre viene de argumentos con clave, esto nos permite indicarle que tendra funcion que reciebn argumento de clave valor

		#mas acciones 
		print("Hemos terminado el calculo.")
#despues de esto debe devolvr una funcion

	return funcion_interior
@funcion_decoradora #con esta instruccion le añade la funcion decoradora

def suma(num1, num2):
	print(num1+num2)


@funcion_decoradora

def resta (num1,num2):
	print(num1-num2)

@funcion_decoradora

def potencia(base, exponente):
	print(pow(base, exponente))

suma(7,5)

resta(8,6)

potencia(base=5, exponente=3)

n1=(int(input("Introduce el primer numero:  ")))
n2=(int(input("Introduce el segundo numero:  ")))

def devuelmax (n1, n2):
	if n1<n2:
		print (n2)
	elif n1>n2:
		print (n1)
	else:
		print("Son iguales")
print ("El numero mas alto es:  ")
devuelmax (n1, n2)

#Ejercicio numero 2
print("Introduzca sus datos personales")

nombre=(input("Nombre: "))
telefono=(input("Telefono: "))
direccion=(input("Direccion: "))

datospersonales=[nombre, telefono, direccion] 

print(f"Los datos personales son: {datospersonales[0]}, {datospersonales[1]}, {datospersonales[2]}") 



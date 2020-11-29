#lower ponemos el nombre en minuscula, capitalize pone la priumera letra en mayuscula
nombreUsuario=input("Introduce un nombre de usuario: ")
print("Nombre de usuario", nombreUsuario.lower())

#isdigit es un booleano y nos sirve para indicar si se introduce numeros con fase y true

edad=input("Introduce tu edad: ")
print(edad.isdigit())


edad=input("Introduce tu edad: ")

while (edad.isdigit()==False):
	print("Por favor, introduce un valor numerico: ")
	edad=input("Introduce tu edad: ")

if (int(edad)<18):
		print("No puedes pasar")
else:
		print("Puedes pasar")
contrasena= input ("Introduce una contraseña: ")
mensaje= "Contraseña ok"

for i in contrasena:
	if(i == " "):
		mensaje= "Contraseña incorrecta"

if (len(contrasena) >8):
	mensaje = "Contraseña incorrecta"

print (mensaje)

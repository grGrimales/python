email=False
#mi_email=input("Introduce tu direccion de correo")
for i in "gredygrimales@gmail.com":
	#print(i)
	if(i=="@"):
		email=True


if email:
	print("El email es correcto")
else:
	print("El email no es corecto")

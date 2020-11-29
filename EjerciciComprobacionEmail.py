email=input("Introduce tu direccion de email: ")
contador_arroba=0
for i in email:
	if i =="@":
		contador_arroba=contador_arroba+1

if contador_arroba==0 or email.startswith("@") or email.rfind("@"):
		print("El correo no es valido")
else:
		print("El correo es correcto")

print(email.rfind("@"))
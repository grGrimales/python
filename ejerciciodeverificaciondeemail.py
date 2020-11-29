email= input("Introduce tu correo electronico por favor: ")
contadorArroba=0
contadorPunto=0

for i in range (len(email)):

	if email[i]=="@":
		contadorArroba=contadorArroba+1

	if email [i]== ".":
		contadorPunto=1
if contadorPunto==0 or contadorArroba!=1:
	print ("email es incorrecto")
else:
	print("Email es correcto")

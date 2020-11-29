def evaluaEdad(edad):

	if edad <0:
		raise ValueError (" La edad no puede ser negativa")

	if edad <20:
		print("Eres muy joven")
	elif edad <40:
		print("Eres joven")
	elif edad <65:
		print("Eres maduro")
	elif edad <100:
		print("Cuidate...")


evaluaEdad(108)

import math 
def calculaRaiz (num1):
	if num1<0:
		raise ValueError (" El numero no puede ser negativa")
	else:
		return math.sqrt (num1)
ope1=(int(input("Introduce un numero: ")))

try:
	print(calculaRaiz(ope1))
except ValueError as ErrorDeNumeroNegativo:
	print (ErrorDeNumeroNegativo)
print("Programa terminado.")
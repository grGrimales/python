i=1

while i<=10:
	print("Ejecucion" + str(i))
	i=i+1

print ("Termino la ejecucion")

edad=int(input("Introduce tu edad por favor: "))

while edad<0:
	print("Has introducido una edad negativa. Vuelve a intentarlo")
	edad=int(input("Introduce tu edad por favor: "))
print ("Gracias por colaborar puedes pasar")
print ("Edad del aspirante " + str(edad))


edad=int(input("Introduce tu edad por favor: "))

while edad<5 or edad>100:
	print("Has introducido una edad negativa. Vuelve a intentarlo")
	edad=int(input("Introduce tu edad por favor: "))
print ("Gracias por colaborar puedes pasar")
print ("Edad del aspirante " + str(edad))

import math
print ("Programa de raiz cuadrada: ")
numero=int(input("Introduce un numero por favor: "))
intentos=0
while numero<0:
	print("No se puede hallar la raiz cuadrada de un numero negativo")

	if intentos==2:
		print ("Has consumido demasiados intentos. El priograma ha finalizado")
		break; 
	numero = int(input ("Introduce un numero por favor: "))
	if numero<0:
		intentos =intentos+1

if intentos <2:
	solucion= math.sqrt(numero)
	
	print("La raiz cuadrada de " + str(numero) + str (intentos))

nombre="Pildoras Informaticas"
contador=0
print(nombre)

for i in nombre:
	if i==" " :
		continue
	contador+=1
print (contador)

email=input("Introduce tu email por favor: ")
for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False
print (arroba)
#bucles for
"""for i in[1,2,3,4]:
	print (i)

for estaciones_año in["primavera", "verano", "invierno", "otoño"]:
	print (estaciones_año)

for i in[1,2,3,4]:
	print ("hola")
#como evitar los saltos de pagina para que aparezca en una misma linea
for i in[1,2,3,4]:
	print ("hola", end="  ")

"""
"""email=False

for i in "Gredygrimales@gmail.com":
	if(i=="@"):
		email=True
if email:
	print("El email es correcto")
else:
	print("El email es incorrecto")

email=False
miEmail=input("Escriba su direccion de email: ")

for i in "Gredygrimales@gmail.com":
	if(i=="@"):
		email=True
if email:
	print("El email es correcto")
else:
	print("El email es incorrecto")

email=False
miEmail=input("Escriba su direccion de email: ")

for i in miEmail:
	if(i=="@"):
		email=True
if email:
	print("El email es correcto")
else:
	print("El email es incorrecto")

contador=0
miEmail=input("Escriba su direccion de email: ")
for i in miEmail:
	if(i=="@"or i=="."):
		contador=contador+1
if contador==2:
	print("El email es correcto")
else:
	print("El email es incorrecto")

#utilizando range
for i in range(5):
	print(i)"""

# Para unir texto convariables:
for i in range(5):
	print(f"valor de la variables{i}")


#Se puede darle mas valores a range:
for i in range(2,10,2):
	print(f"valor de la variables{i}")

	#Utilizando la funcion len:
correcto = False

email=input("Introduce tu email: ")

for i in range(len(email)):

	if email[i]=="@":
		correcto=True
if correcto:
	print("El email es correcto")
else:
	print("El email es invalido")


	







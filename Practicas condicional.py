#utilizamo str para convertir una valor entero en un texto
salario_presidente =int(input("Introduce salario presidente: "))
print ("Salario_presidente: "+ str (salario_presidente))

salario_director =int(input("Introduce salario director: "))
print ("salario_director: "+ str (salario_director))

salario_jefe_area =int(input("Introduce salario jefe de area: "))
print ("salario_jefe_area: "+ str (salario_jefe_area))

salario_administrativo =int(input("Introduce salario administrativo: "))
print ("salario_administrativo: "+ str (salario_administrativo))

#Concatenacion de operadores de comparacion:

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
 print("Todo esta funcionanado correctamente")

else:
 print("Algo esta fallando en esta empresa")

 #utilizando el operador "and" que puede ser traducido como: y si ademas

 print("Programa de becas año 2020 ")

 distancia_escuela=int(input("Indica la distancia a la escuela en km "))
 
 numero_hermanos=int(input("Indica cuantas hermanos tienes "))

 salario_familiar=int(input("Indica el salario bruto anual "))

 if distancia_escuela>40 and numero_hermanos >2 and salario_familiar <=20000:

 	print("Tienes derecho a la beca")
 else:
 	print("No tienes acceso a la beca")

 #Utilizando el operador "or" que se puede traducir como: "o si no"
 
 print("Programa de becas año 2020 ")

 distancia_escuela=int(input("Indica la distancia a la escuela en km "))
 
 numero_hermanos=int(input("Indica cuantas hermanos tienes "))

 salario_familiar=int(input("Indica el salario bruto anual "))

 if distancia_escuela>40 and numero_hermanos >2 or salario_familiar <=20000:

 	print("Tienes derecho a la beca")
 else:
 	print("No tienes acceso a la beca")

 #utilizando el operador in
print ("Asignaturas opcionales año 2020")
print("Asignaturas opcionales: Arte- Reposteria- Diseño- Peluqueria")
opcion=(input("Escribe la asigantura escogida "))
#como transformar un texto pedidio por teclado a minusculas:
lista_asignatura = ("arte", "reposteria", "diseño", "peluqueria")
asignatura=opcion.lower()
#print(asignatura)

if asignatura in lista_asignatura:
	print(" Asignatura escogida " + asignatura)

else:
	print("La asignatura escogida no esta contemplada")
	
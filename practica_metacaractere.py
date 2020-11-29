import re

listas_nombres=['Ana Gomez',
				'Lucía Guzman',
				'Saymon Calvo',
				'Carlos Guzman',
				'Grediana de Guzman',
				'Lucía Rojas',
				'camion',
				'camión',
				'Saymon Rojas']

for elemento in listas_nombres:
	if re.findall('^Lucía', elemento): #este ^ esta es un ancla lo que hace es buscar todas las palabras que empiecen con el nombre que se le indique  
		print(elemento)
for elemento in listas_nombres:
	if re.findall('Guzman$', elemento):# esta es otra anclacolocado al final $ busca a todas las palabras que terminen con ese nombre
		print(elemento)

for elemento in listas_nombres:
	if re.findall('[n]', elemento): 
		print(elemento)
#utilizando el metacaracter [] nos busca todas las palabras que contenga ese elemento
print("Esta es otra forma de uso")

for elemento in listas_nombres:
	if re.findall('cami[oó]n', elemento): #de esta forma nos busca palabras que empiecen por cami luego que contenga lo que esta dentro del corchete y terminen en la letra que indiquemos
		print(elemento)
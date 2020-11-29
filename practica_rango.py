import re

listas_nombres=['Ana Gomez',
				'Lucía Guzman',
				'Saymon Calvo',
				'Carlos Guzman',
				'Grediana de Guzman',
				'Lucía Rojas',
				'Saymon Rojas']

for elemento in listas_nombres:
	if re.findall('^[A-t]', elemento): 
		print(elemento)
#con el rango nos busca los nombre que esten comprendidos entre la letra por ejemplo de la o a la t

listas_nombres=['Per1',
				'Per2',
				'Per3',
				'Ven1',
				'Ven3',
				'Per4',
				'PerA',
				'PerB',
				'PerC',
				'Mar4']
for elemento in listas_nombres:
	if re.findall('Per[0-2A-B]', elemento): #esta es otra forma de buscar con rango
		print(elemento)			

#otra forma seria indicandole lo siguiente if re.findall('Per[.:]', elemento): nos buscaria palabra que empiencen por ejemplo en este caso con per y que contengan despues . o :
def generaPares (limite):

	num=1
	miLista=[]

	while num<limite:
		miLista.append(num*2)

		num=num+1
	return miLista

print (generaPares(9))

def generaPares (limite):

	num=1
	while num<limite:
		yield num*2
	
		num=num+1
devuelvePares=generaPares(10)

print (next (devuelvePares))

print("Aqui podria ir mas codigo...")

print(next (devuelvePares))

print ("Aqui podria ir mas codigo...")

print(next (devuelvePares))

def devuelve_ciudades (*ciudades):
	for ciudad in ciudades:
		yield from ciudad
ciudades_devueltas = devuelve_ciudades("La Asuncion","Juan Griego", "Santa Ana", "Porlamar")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
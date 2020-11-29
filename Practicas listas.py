miLista=["Grediana", "Lucia", "Saymon","Carlos" ]
print(miLista[:])

#acceder a un elemento en concreto por indice
print(miLista[3])

#se puede acceder a los indices de la lista contando desde atras hacia adelante empezando desde 1
#y con el signo-1
print(miLista[-3])

#para acceder a una porción de la lista:
print(miLista[0:3])

#como agregar un elemento a una lista
miLista.append("Gollo")
print(miLista[:])

#como agregar un elemento a una lista en un indice especifico
miLista.insert(2,"Miladys")
print(miLista[:])

#para agregar varios elemento a una lista
miLista.extend(["Alexander", "Gregorio"])
print(miLista[:])

#para buscar el numero de indice de un elemento de la lista
#si hay elementos duplicados en la lista, devuelve el numero del primer elemento.
print(miLista.index("Alexander"))

#Como saber si un elemento se encuentra en la lista
print("Pepe" in miLista)
print("Grediana" in miLista)

#Para eliminar elementos de una lista
miLista.remove("Alexander")
print(miLista[:])

#eliminar el ultimo elemento de la lista
miLista.pop()
print(miLista[:])

#para unir dos listas diferentes
miLista2 =["Alexander", 1, True, 3.5 ]
miLista3=miLista + miLista2
print(miLista3)

#Para repetir una lista
miLista4 =miLista * 3
print(miLista4)

 
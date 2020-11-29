#las tuplas son lista inmutables es decir no se pueden cambiar
mitupla=("Grediana", 7, 1, 1993)
#para buscar un indice en las listas
print(mitupla[1])

#Convertir una tupla en lista
milista=list(mitupla)
print(milista [:])

#convertir una lista en tupla
milista=("Grediana", 7, 1, 1993)
mitupla=tuple (milista)
print (mitupla)

#Contar cuantas veces hay un elemento en una tupla

print(mitupla.count("Carlos"))

#Saber la longitud de una tupla ver cuantos elementos hay

print (len(mitupla))

#desempaquetado de tuplas
nombre, dia, mes, ano = mitupla
print(nombre)
print(dia)
print(mes)
print(ano)

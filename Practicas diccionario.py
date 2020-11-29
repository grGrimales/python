midiccionario={"Alemania" : "Berlin", "Francia" : "Paris", "Venezuela" : "Caracas", "Peru" : "Lima"}
#Para acceder a una valor de un diccionario por su clave
print(midiccionario ["Peru"])

#como agregar nuevos elementos al diccionario


midiccionario ["Italia"] = "Lisboa"

#sobreescribir un elemento

midiccionario ["Italia"] = "Roma"
print(midiccionario)

#Como eliminar un elemento

del midiccionario ["Alemania"]
print(midiccionario)

# Pasar las claves del diccionario de una lista
paises = ["Peru", "Colombia", "Venezuela"]


midiccionario2 ={paises [0] : "Lima", paises[1]: "Bogota", paises[2] : "Caracas"}
print(midiccionario2)

#Como imprimir las claves, valores y longitud de un diccionario:

print(midiccionario.keys())

print(midiccionario.values())

print(len(midiccionario))



def areaCuadrado(lado):
	"""calcula el area cuadrada de un cuadrado, elevando al cuadrado el lado
	pasado por parametro"""
	return "El area del cuadrado es: " + str(lado*lado)

def areaTriangulo(base,altura):
	return "El area del triangulo es: " + str((base*altura)/2)

print(areaCuadrado(3))

print(areaTriangulo(4,6))

print(areaCuadrado.__doc__) 
#con esta instruccion nos imprime la documentacion que tenemos
help(areaCuadrado) #con esta instruccion tambien nos imprime la documentacion
"""en caso que tengamos una clase la forma de buscar la ayuda de la funcion es la siguiente: 
help(elnombredela clase.elnombredelafuncion)
tambien podemos pedir la informacion de toda la clase: help(nombredelaclase)
----Para comprabar que una funcion funcione correctamente podemos verificarlo con la documentacion
 de la siguiente forma:"""
def areaTriangulo2(base,altura):
	"""calcula el area del trinangulo
	>>>areaTriangulo2(3,6)
	9.0

	"""
	return "El area del triangulo es: " + str((base*altura)/2)

import doctest 

doctest.testmod()


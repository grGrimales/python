#las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda por ejemplo el formato de un correo 
#para utilizar la expresiones debemos importar el modulo re

import re 

cadena="Vamos aprender expresiones regulares"

textoBuscar="aprender"

if re.search(textoBuscar, cadena) is not None:
	print("he encontrado el texto")

else:
	print("No he encontrado el texto")

#print(re.search("aprender", cadena)) #el metodo search permite dos parametros  que palabra buscara y en donde devuleve un none si no encuentra
cadena="Vamos aprender expresiones regulares en python. python es un lenguaje de aprendizaje sencillo."

textoBuscar="python"

textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start()) # el metodo start lo que hace es indicarno en que nuemero de caracter se encuentra la palabra buscada
print(textoEncontrado.end()) #end nos devuelve el ultimo caracter donde se encuentra 
print(textoEncontrado.span())#el metodo span nos devuelve en una tupla  la funcion de start y end
print(len(re.findall(textoBuscar, cadena))) #el metodo findall nos devuelve la cantidad de veces que este escrita la palabra buscada y con len nos devuelve en numero 

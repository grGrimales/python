#la funcion match lo que hace es buscar si hay una coincidencia wn un patron  busqueda al comienzo de una cadena de texto siempre es al comienzo
import re 
nombre1="lucia Guzman"
nombre2="Saymon Calvo"
nombre3="Grediana de Guzman"

if re.match("Lucia", nombre1, re.IGNORECASE): 
#esta funcion admite tres parametros el tercer parametro es para que no sea sensible a mayusculas y minusculas
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")
#otra forma de aplicarla seria:

if re.match(".ucia", nombre1, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

#tambien podemos utilizarlo asi:/\d con esto le indicamos que busque si delante hay un numero o no if re.match("i\d", nombre1):
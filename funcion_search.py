#la funcion search busca en toda la cadena de texto el patron de busqueda, esta funcion tambien admite tres parametros
import re 
nombre1="Lucia Guzman"
nombre2="Saymon Calvo"
nombre3="Grediana de Guzman"

if re.search("Guzman", nombre1): 
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")
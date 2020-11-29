#creando un archivo externo en modo escritura
from io import open
archivo_texto=open ("archivo.txt", "w")
frase=" Estupendo dia para aprender python \n Viernes "

archivo_texto.write(frase)
archivo_texto.close
#creando un archivo externo en modo lectura

from io import open
archivo_texto=open ("archivo.txt", "r")
texto=archivo_texto.read()
archivo_texto.close
print(texto)


#como acceder a cada linea del texto:
from io import open
archivo_texto=open ("archivo.txt", "r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close
print(lineas_texto[0])

#como agregarle informacion al texto utilizando a de append:
from io import open
archivo_texto=open ("archivo.txt", "a")
archivo_texto.write("\n  Con esfuerzo y dedicacion podemos seguir aumentando nuestros conocomientos")
archivo_texto.close

#para leer todo el archivo de texto

from io import open
archivo_texto=open ("archivo.txt", "r")
print(archivo_texto.read())
archivo_texto.close

#como hacer para cambiar la posicion del puntero en el archivo de texto con el metodo seek:

from io import open
archivo_texto=open ("archivo.txt", "r")
print(archivo_texto.read())
archivo_texto.seek(0)
print(archivo_texto.read()


#como hacer para situarnos en la mitad del texto:

from io import open
archivo_texto=open ("archivo.txt", "r")
archivo_texto.seek(len(archivo_texto.read())/2)
print (archivo_texto.read())
archivo_texto.close

#como hacer para situarnos al final de la primera linea con el metodo readline:
from io import open 
archivo_texto=open ("archivo.txt", "r")
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())
archivo_texto.close

from io import open 
archivo_texto=open ("archivo.txt", "r+") #archivo de lectura y escritura
lista_texto=archivo_texto.readlines();
lista_texto[1]="Esta linea de texto ha sido incluida desde el exterior \n"
archivo_texto.seek (0)
archivo_texto.writelines(lista_texto)
archivo_texto.close
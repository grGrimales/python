import pickle 
listas_nombres=["Carlos", "Grediana", "Saymon", "Lucia"]

fichero_binario=open ("listas_nombres", "wb")

pickle.dump(listas_nombres, fichero_binario) #el metodo dump lo realizamos para importar la informacion de la lista al archivo de texto

fichero_binario.close()
del(fichero_binario) #esta funcion la utilizamos para borrarlo de la memoria

import pickle 
carpeta=open ("listas_nombres", "rb")
lista=pickle.load(carpeta) #con el metodo load logramos rescatar la informacion que esta alamacenada en codigo binario
print(lista)
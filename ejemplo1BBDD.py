import sqlite3

miConexion=sqlite3.connect("PrimeraBase")#el primer paso  es abrir y crear la conexion 

miCursor=miConexion.cursor() # este es el segundo paso crear un cursor o puntero

#miCursor.execute("CREATE TABLE PRODUCTOS1( NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER , SECCION VARCHAR (20))")
#VARCHAR LO UTILIZAMOS PARA INDICAR QUE ES TEXTO Y DEBEMOS INDICAR LA CANTODAD DE CARACTERES DENTRO DEL PARENTESIS
#INTEGER LOS UTILIZAMOS PARA INDICAR QUE ALMACENAREMOS ENTEROS

#miCursor.execute("INSERT INTO PRODUCTOS1 VALUES('BALON', 15, 'DEPORTES')")
#EL METODO execute lo utilizamos para agregar informacion a la tabla

#variosProductos=[ #con esta lista podemos insertar mas informacion creando en su interior una tupla()
#("Camiseta", 10, "Deportes"),
#("Jarron", 90, "Ceramicas"),
#("Camión", 20, "Juguetería")

#]


miCursor.execute("SELECT * FROM  PRODUCTOS")
variosProductos=miCursor.fetchall()#este metodo lo utilizamos para leer la informacion de la tabla nos devuleve una lista con toda la informacion de los productos 
for  producto in variosProductos:
	print(producto)
#tambien podemos acceder a informacion especifica accediendo a su indice y si queremos concatenarlo ejemplo: print(producto[0], producto[2])





#miCursor.executemany("INSERT INTO PRODUCTOS1 VALUES(?,?,?)", variosProductos)
#CON ESTE METODO PODEMOS INSERtar mucha  informacion como una lista y dentro de VALUES se escribe signos interragacion de acuerdo al numero de item que se esten ingresando 
miConexion.commit()
miConexion.close()#el ultimo es cerrar la conexion

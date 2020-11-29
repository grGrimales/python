import sqlite3 

miConexion=sqlite3.connect("Gestion de Productos2")

miCursor=miConexion.cursor()


miCursor.execute('''
	CREATE TABLE PRODUCTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
	PRECIO INTEGER,
	SECCION VARCHAR (20))
''')
#COLACANDO LA PALABRA UNIQUE LE INDICAMOS QUE EL CAMPO DE ESA COLUMNA NO SE PUEDE REPETIR
productos=[
	("Pelota", 20, "Juguetería"),
	("Pantalon", 20, "Confeccion"),
	("Destornillador", 25, "Ferreteria"),
	("Jarron", 30, "Cerámica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)


miConexion.commit()
miConexion.close()

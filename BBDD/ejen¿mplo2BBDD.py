import sqlite3 

miConexion=sqlite3.connect("Gestion de Productos")

miCursor=miConexion.cursor()


miCursor.execute('''
	CREATE TABLE PRODUCTOS(
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY, 
	NOMBRE_ARTICULO VARCHAR(50), 
	PRECIO INTEGER,
	SECCION VARCHAR (20))
''')
#PRIMARY KEY INDICAMOS QUE ES EL CAMPO CLAVE
productos=[
	("AR01", "Pelota", 20, "Juguetería"),
	("AR02", "Pantalon", 20, "Confeccion"),
	("AR03", "Destornillador", 25, "Ferreteria"),
	("AR04", "Jarron", 30, "Cerámica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)", productos)


miConexion.commit()
miConexion.close()

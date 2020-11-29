import sqlite3 

miConexion=sqlite3.connect("Gestion de Productos2")

miCursor=miConexion.cursor()

miCursor.execute("UPDATE PRODUCTOS  SET PRECIO=35 WHERE NOMBRE_ARTICULO= 'Pelota'")

miConexion.commit()
miConexion.close()
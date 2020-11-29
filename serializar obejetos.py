import pickle
class Vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar (self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frena (self):
		self.frena=True 

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena)

coche1=Vehiculos ("Mazda", "MX5")

coche2=Vehiculos("Seat", "lenon")

coche3=Vehiculos ("Renault", "Megane")

coches=[coche1, coche2,coche3]

fichero= open("LosCoches", "wb") #esto lo realizamos para abrir el archivo de texto bianrio

pickle.dump(coches, fichero) #para hacer el volcado de la informacion utilizamos el metodo dump de la la biberia pickle

fichero.close()

del (fichero)

ficheroApertura=open ("LosCoches", "rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches: 
 	print (c.estado())
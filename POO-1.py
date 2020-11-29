class Coche():
	largoChasis=200
	anchoChasis=120
	ruedas=4
	enmarcha=False

	def arrancar(self, arrancamos):
		self.enmarcha=arrancamos

		
		if (self.enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

	def estado (self):
		print("El coche tiene ", self.ruedas, "ruedas. un ancho de: ", self.anchoChasis, "y un largo de",
			self.largoChasis)
	
miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print ("---------Creamos el segundo objeto-----------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche.estado()
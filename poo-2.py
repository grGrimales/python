#Para crear un metodo constructor de estado inicial para obejtos con la misma clase:def __init__(self):
#Para encapsular una variedad o propiedad colocamos dos guiones bajos:self.__ruedas=4
class Coche():
	def __init__(self):
		self.largoChasis=200
		self.anchoChasis=120
		self.__ruedas=4
		self.enmarcha=False

	def arrancar(self, arrancamos):
		self.enmarcha=arrancamos
		if (self.enmarcha):
			chequeo=self.__chequeo_interno()
		if (self.enmarcha and chequeo):
			return "El coche esta en marcha"
		elif (self.enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo. No podemos arrancar"
		else:
			return "El coche esta parado"

	def estado (self):
		print("El coche tiene ", self.__ruedas, "ruedas. un ancho de: ", self.anchoChasis, "y un largo de",
			self.largoChasis)
	def __chequeo_interno(self):
		print("Realizando chequeo interno")
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"
		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False
		
		
miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print ("---------Creamos el segundo objeto-----------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche.estado()
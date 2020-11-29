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

class Velectrico(Vehiculos):
	def __init__(self, marca,modelo):
		super().__init__(marca, modelo)
		self.autonomia=100


	def cargarEnergia(self):
		self.cargando=True


class Furgoneta(Vehiculos):
	def carga (self, cargar):
		self.cargado=cargar
		if (self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"

class Moto(Vehiculos):
	def caballito (self):
		self.hcaballito="Voy haciendo el caballito"
	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena, "\n", self.hcaballito)
	
class BicletaElectrica (Velectrico, Vehiculos):
	pass


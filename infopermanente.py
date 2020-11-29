import pickle 
class Persona:
	def __init__(self, nombre,genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado a una persona con el nombre de: ", self.nombre)
	def __str__(self):
		return "{}, {}, {}".format(self.nombre, self.genero, self.edad)

class ListasPersonas:
	personas=[]
	def __init__(self):
		listaDePersona=open("ficheroExterno", "ab+")#esto lo utilizamos para crear nuestro fichero externo y aregar informacion permanentemente
		listaDePersona.seek(0)#para desplazar el pulsor a la posicion de inicio
		
		try:
			self.personas=pickle.load(listaDePersona)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

		except:
			print("El fichero esta vacio")
		finally:
			listaDePersona.close()
			del(listaDePersona)
	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonaEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonaEnFicheroExterno(self):
		listaDePersona=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersona)
		listaDePersona.close()
		del(listaDePersona)
	def mostrarInfoFicheroExterno(self):
		print("La informacion del fichro externo es la siguiente: ")
		for p in self.personas:
			print(p)

miLista=ListasPersonas()
persona=Persona("Grediana", "femenino", 23)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
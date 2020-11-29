
#la funcion filter verifica que los elementos de una secuencia cumplen una condicion 
#devolviendo un iterador con los elemntos que cumplen dicha condicion.  con ayuda de la funcion lambda
class Empleado:


	def __init__(self, nombre, cargo, salario):

		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario) 

listaEmpleados=[
Empleado("Lucia", "Arquitecto", 80000),

Empleado("Saymon", "Abogado", 80000),

Empleado("Carlos", "Estadistico", 30000),

Empleado("Grediana", "Programadora", 30000)
]


salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:
	print(empleado_salario)
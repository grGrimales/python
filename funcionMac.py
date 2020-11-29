#la funcion mac aplica una funcion a cada elemento de una lista iterable devolviendo una lista con los resultado


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

def calculo_comision (empleado):
	empleado.salario=empleado.salario*1.03
	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
	print (empleado)
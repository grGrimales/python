#la funcion lambda es una funcion anonima y se utiliza  para abreviar la sintaxis

#-------------funcion tradicional---------------
def area_triangulo( base, altura):

	return(base*altura)/2

print(area_triangulo(5,7))
#---------------funcion lambda-----------------	

area_triangulo=lambda base,altura:(base*altura)/2
triangulo1=area_triangulo(7,5)
triangulo2=area_triangulo(9,6)

print(triangulo2)

destacar_valor=lambda comision:"¡{}! $".format(comision)

comision_Ana=15855

print(destacar_valor(comision_Ana))
#print ("Inicia programa de evaluacion de alumnos")

#nota_alumno = input ("Introduce la nota del alumno ")

#def evaluacion (nota):
#	Valoracion= "Aprobado"

#	if nota < 5:
#		Valoracion= "Reprobado"

#	return Valoracion

#print (evaluacion(int(nota_alumno)))

print ("Inicia programa de evaluacion de alumnos")

nota_alumno= input ("Introduce la nota del alumno")

def evaluacion(nota):
	Valoracion= "Aprobado"

	if nota < 5:
		Valoracion = "Reprobado"
	return Valoracion

print (evaluacion(int(nota_alumno)))
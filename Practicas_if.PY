#Condicional IF
print ("Inicia programa de evaluacion de alumnos")

#Introducir un valor por teclado
nota_alumno = input ("Introduce la nota del alumno")

def evaluacion(nota):
	valoracion = "Aprobado"

	if nota < 5:
		valoracion = "Reprobado"

	return valoracion

print (evaluacion(int(nota_alumno)))



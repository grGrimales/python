print ("verificacion de acceso")
edad_usuario= int (input("Introduce tu edad por favor "))

if edad_usuario <18:
	print ("No puedes pasar")

else:
	print ("Puedes pasar")

print ("El programa ha finalizado")


# Para evaluar varias condiciones 
print ("verificacion de acceso")
edad_usuario= int (input("Introduce tu edad por favor "))

if edad_usuario <18:
	print ("No puedes pasar")
elif edad_usuario >100:
	print ("Edad incorrecta")

else:
	print ("Puedes pasar")

print ("El programa ha finalizado")

print ("verificacion de acceso")

nota_alumno = int (input("Introduce tu nota, por favor "))

if nota_alumno <5:
	print ("Reprobado")
elif nota_alumno <6:
	print ("Deficiente")
elif nota_alumno<7 :
	print ("Regular")
elif nota_alumno <9:
	print ("avanzado")
else:
 print ("Sobresaliente")


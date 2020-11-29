def divide ():
	try:
		num1=(float(input("Introduce el primer valor: ")))
		num2=(float(input("Introduce el segundo valor: ")))
		print("Este es el resultado" + str (num1/num2))
	except ValueError:
		print("El valor introducido es erroneo")
	except ZeroDivisionError:
		print("No se puede dividir entre 0!")

	print("La operacion ha finalizado")
divide ()
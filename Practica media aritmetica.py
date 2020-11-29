n1= (int(input("Introduce el primer numero ")))
n2=(int(input("Introduce el segundo numero ")))
n3=(int(input("Introduce el tercer numero ")))


def mediaArtimetica(numero1, numero2, numero3):

	suma_numeros = numero1 + numero2 + numero3

	return suma_numeros/3



media_aritmetica =mediaArtimetica(n1,n2,n3)
print("La media aritmetica es: ")
print (media_aritmetica)
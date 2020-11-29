def compruebaMail(mailUsuario):
	"""
	La funcion comprueba  un email recibido y verifica
	si tiene @. Si tiene una @ es correcto, si tiene mas de uno
	es incorrecto, si esta al final es incorrecto.
	>>> compruebaMail('gredy@gmail.com')
	True

	>>> compruebaMail('gredygmail.com')
	False

	>>> compruebaMail('gredygmail.com@')
	False

	>>> compruebaMail('gredy@gmail@com')
	False
	"""

	arroba=mailUsuario.count('@')
	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True

import doctest 

doctest.testmod()

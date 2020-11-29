from tkinter import*
from tkinter import messagebox #esta libreria la importamos para crear las ventanas emergentes
root=Tk()


def infoAdicional():
	messagebox.showinfo("Procesador de Grediana", "Procesador de texto 2020")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	#valor=messagebox.askquestion("Salir", "¡Deseas salir de la aplicacion?") con este metodo nos pregunta si o no y nos devuelve yes o not
	#if valor=="yes":
	valor=messagebox.askokcancel("Salir", "¡Deseas salir de la aplicacion?")
	if valor==True:
		root.destroy() #esta funcion nos permite salir de la aplicacions
def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado.")
	if valor==False:
		root.destroy()
barraMenu=Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)#tearoff=0 con esta funcion logramos desaparecer la linea horizontal que aparece
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


archivoHerramientas=Menu(barraMenu,tearoff=0)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
#barraMenu.add_cascade con este metodo le colocamos el nombre a la barra de menu

barraMenu.add_cascade(label="Edición", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()
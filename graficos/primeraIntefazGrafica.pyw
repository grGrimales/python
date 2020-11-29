from tkinter import * #tkinter es la libreria que utilizaremos para las interfaces graficas

raiz=Tk()

raiz.title("Ventana de pruebas") #con el metodo title se le coloca titulo a la ventana

#raiz.resizable(0,0)#el metodo resizable nos permite modificar el tamaño de la ventana,recibe por parametros valores booleanos 0 equile a false el de la izquierda es width ancho y el de la derecha height alto
raiz.iconbitmap("Luz.ico.ico") #con este metodo agregamos imagenes

#raiz.geometry("650x350") #para cambiar las dimensiones de la ventana

raiz.config(bg="green") #para cambiar el color del fondo

miFrame=Frame() # creamos nuestro variable y nuestro  frame.

miFrame.pack() # (side="left", anchor="n")con esto logramos empaquetar el frame para que este dentro de la raiz colocando los parametros logramos ubicarlo bien sea ala derecha abjo izuierda
#con el metodo fill="y" and "True" logramos que se expanda verticalmente por  la raiz
#con el metodo fill="both" and "True" se expande por toda la raiz
miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35) #con esto establecemos un grosor para el borde

miFrame.config(relief="groove")# con esto le indicamos que queremos un borde. este metodo es otro tipo de borde relief="sunken"

miFrame.config(cursor="pirate") #con ello logramos cambiar la forma del cursor

raiz.mainloop() #el metodo mainloop lo utilizamos para crear una ventana, este metodo funciona como un bucle infinito


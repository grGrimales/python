from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo (request): #primera vista
    p1= Persona("Lucia", "Rojas")
    temas1= ["Tablas", "Vistas","URL"]
    fecha_actual=datetime.datetime.now()
    #doc_Externo=open("C:/Users/Guzmán/Documents/ProyectoDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    #plt= Template(doc_Externo.read())
    #doc_Externo.close()
    #Creamos una variable con el metodo loader.get_template('pasandole por parametro el nombre de la plantilla')
    #doc_externo=loader.get_template('miplantilla.html')
    #ctx= Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual":fecha_actual, "temas":temas1})
    #documento= doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual":fecha_actual, "temas":temas1} )

    return render(request, "miplantilla.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual":fecha_actual, "temas":temas1})

def cursoC(request):
   fecha_actual=datetime.datetime.now()
   return render(request, "cursoC.html", {"dameFecha":fecha_actual})

def cursoCss(request):
   fecha_actual=datetime.datetime.now()
   return render(request, "cursoCSS.html", {"dameFecha":fecha_actual})

def despedida(request):
    return HttpResponse("Nos vemos pronto.")
#%s es un marcador de posicion

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales: %s 
    </h1>
    </body>
    </html> """ % fecha_actual
    return HttpResponse(documento)

def calcula_edad(request, edad, agno):
    edad_actual=edad
    periodo=agno-2020
    edad_futura=periodo+edad_actual
    documento="""<html>
    <body>
    <h1>
    En el año %s tendras %s 
    </h1>
    </body>
    </html> """ %(agno, edad_futura) 
    return HttpResponse(documento)
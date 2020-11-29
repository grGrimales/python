from django.shortcuts import render, HttpResponse
from RecetasApp.models import Recetario

# Create your views here.
def inicio(request):
    return render(request, "RecetasApp/inicio.html")

def recetario(request):
    receta=Recetario.objects.all()
    return render(request, "RecetasApp/recetario.html", {"receta":receta})

def contacto(request):
    return render(request, "RecetasApp/contacto.html")
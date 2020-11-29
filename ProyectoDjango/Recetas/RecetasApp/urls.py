from django.urls import path
from RecetasApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('contacto',views.contacto, name="Contacto"),
    path('recetario',views.recetario, name="Recetario"),

]


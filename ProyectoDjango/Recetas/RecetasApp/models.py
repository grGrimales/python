from django.db import models

# Create your models here.
class Recetario(models.Model):
    receta=models.CharField(max_length=80)
    ingredientes=models.CharField(max_length=150)
    preparacion=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='demostracion')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name='recetario'
        verbose_name_plural='recetarios'
    def __str__(self):
        return  self.receta
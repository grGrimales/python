from django.contrib import admin
from RecetasApp.models import Recetario
# Register your models here.
class RecetarioAdmin(admin.ModelAdmin):
    list_display=("receta", "ingredientes", "preparacion")
    list_filter=("receta",)
    readonly_fields=('created', 'updated')
admin.site.register(Recetario, RecetarioAdmin)
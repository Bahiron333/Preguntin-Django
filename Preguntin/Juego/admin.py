from django.contrib import admin
from Juego.models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("Nombre_Categoria",)
    exclude = ('Id_Categoria',) #sea excluido de la categoria (No se muestre)

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("Nombre_pregunta","Id_Categoria")
 


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)

#personalizacion deladministrador
admin.site.site_title = 'Preguntin - Administrador'
admin.site.site_header = 'Preguntin'
admin.site.index_title = 'Administracion'

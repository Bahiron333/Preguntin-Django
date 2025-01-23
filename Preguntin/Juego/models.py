from django.db import models
from Jugador.models import Usuario

# Create your models here.

class Categoria(models.Model):


    Nombre_Categoria = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.Nombre_Categoria


class Pregunta(models.Model):

    Id_Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) #clave foranea de Categoria y si se borra sera en cascada
    Nombre_pregunta = models.CharField(max_length=200, unique=True)
    Opcion_A = models.CharField(max_length=100)
    Opcion_B = models.CharField(max_length=100)
    Opcion_C = models.CharField(max_length=100)
    Opcion_D = models.CharField(max_length=100)
    Respuesta_Corecta = models.CharField(max_length=30)
    Puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.Nombre_pregunta #se envia como cadena de texto 


class Puntaje(models.Model):
    Id_Jugador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

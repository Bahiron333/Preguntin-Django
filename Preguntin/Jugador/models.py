from django.db import models

# Create your models here.

class Usuario(models.Model):

    Nombre_Usuario = models.CharField(max_length=30)
    passworld = models.CharField(max_length=100)


class informacion_contacto(models.Model):

    Id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #llave foranea de usuario
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    adress = models.CharField(max_length=30)



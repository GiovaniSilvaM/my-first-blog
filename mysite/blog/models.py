from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre =  models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=8)


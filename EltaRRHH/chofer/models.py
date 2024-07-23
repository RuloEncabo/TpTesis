
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from RRHH import settings

class Chofer(models.Model):
    Id_chofer= models.AutoField(primary_key=True)
    #legajo = models.CharField(max_length=100,null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    calle = models.CharField(max_length=100)
    nrocalle = models.CharField(max_length=10)
    piso = models.CharField(max_length=10, null=True, blank=True)
    departamento = models.CharField(max_length=10, null=True, blank=True)
    barrio = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    cp = models.CharField(max_length=10)
    movil = models.CharField(max_length=15)
    contactoemergencia = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    ingresoFCA_venc = models.DateField()
    licencia_venc = models.DateField()
    psicofisico_venc = models.DateField()
    curso_venc = models.DateField()
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
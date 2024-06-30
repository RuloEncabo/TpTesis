from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager    

# Create your models here.
class Chofer(models.Model):
    Id_chofer = models.IntegerField(primary_key=True)
    Legajo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    calle = models.CharField(max_length=100, unique=True)
    nrocalle = models.CharField(max_length=10)
    piso = models.CharField(max_length=10)
    Deptartamento = models.CharField(max_length=10)
    barrio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=80)
    provincia = models.CharField(max_length=10)
    cp = models.IntegerField()
    movil = models.CharField(max_length=15)
    contactoemergencia = models.CharField(max_length=80)
    parentesco = models.CharField(max_length=80,blank=True)
    foto = models.ImageField(upload_to='fotochofer/', blank=True)   
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_activo = models.BooleanField(default=True)
    
    
def __str__(self):
    return self.apellido

#usario, procreso, fecha, datos anteior, dato actual 

#control lote de movimeintos.
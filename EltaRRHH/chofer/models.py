
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class MyChoferManager(BaseUserManager):
    def create_chofer(self, first_name, last_name, username, email, phone_number, password=None):
        if not email:
            raise ValueError('Ingrese Correo Electrónico')
        if not username:
            raise ValueError('Ingrese Nombre de Usuario')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user




class Chofer(models.Model):
    Id_chofer = models.AutoField(primary_key=True)  # Cambié a AutoField para generación automática
    Legajo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    calle = models.CharField(max_length=100)
    nrocalle = models.CharField(max_length=10)
    piso = models.CharField(max_length=10, blank=True)
    departamento = models.CharField(max_length=10, blank=True)  # corregí 'Deptartamento' a 'departamento'
    barrio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=80)
    provincia = models.CharField(max_length=10)
    cp = models.IntegerField()
    movil = models.CharField(max_length=15)
    contactoemergencia = models.CharField(max_length=80)
    parentesco = models.CharField(max_length=80, blank=True)
    foto = models.ImageField(upload_to='fotochofer/', blank=True)
    ingresoFCA_venc = models.DateField(default=date(2025, 1, 1))
    licencia_venc = models.DateField(default=date(2025, 1, 1))  # nuevo campo
    psicofisico_venc = models.DateField(default=date(2025, 1, 1))  # nuevo campo
    curso_venc = models.DateField(default=date(2025, 1, 1))

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
from django.apps import apps
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from datetime import date

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, phone_number, password=None, role=None):
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
        user.role = role
        user.save(using=self._db)

        if role == 'chofer':
            UsuarioChofer = apps.get_model('usuarios', 'UsuarioChofer')
            UsuarioChofer.objects.create(
                usuario=user,
                dni="00000000",
                calle="Calle Ejemplo",
                nrocalle="123",
                piso="1",
                departamento="A",
                barrio="Barrio Ejemplo",
                localidad="Localidad Ejemplo",
                provincia="Provincia Ejemplo",
                cp="1234",
                contactoemergencia="Contacto Ejemplo",
                parentesco="Parentesco Ejemplo",
                foto=None,
                ingresoFCA_venc=date(2025, 1, 1),
                licencia_venc=date(2025, 1, 1),
                psicofisico_venc=date(2025, 1, 1),
                curso_venc=date(2025, 1, 1)
            )

        return user

    def create_superuser(self, first_name, last_name, username, email, phone_number, password=None):
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('chofer', 'Chofer'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=128, default='123456789')
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True, default='default_username')
    password = models.CharField(max_length=120)
    role = models.CharField(max_length=10, choices=ROLES, default='chofer')
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']
    
    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
class UsuarioChofer(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    dni = models.CharField(max_length=10)
    calle = models.CharField(max_length=100)
    nrocalle = models.CharField(max_length=10)
    piso = models.CharField(max_length=10, blank=True, null=True)
    departamento = models.CharField(max_length=10, blank=True, null=True)
    barrio = models.CharField(max_length=100, blank=True, null=True)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    cp = models.CharField(max_length=10)
    contactoemergencia = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='choferes/fotos/', blank=True, null=True)
    ingresoFCA_venc = models.DateField()
    licencia_venc = models.DateField()
    psicofisico_venc = models.DateField()
    curso_venc = models.DateField()
    
    def __str__(self):
        return self.usuario.first_name
    
    def direccion(self):
        return f'{self.calle}{self.nrocalle} {self.piso}'
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager    

# Create your models here.

#clase para generar usuarios
class MyAccontManager(BaseUserManager):
    #funcion que permite crear un nuevo usuario 
    def create_user(self,first_name,last_name, email, username,password=None):
        #muestra error si el usuario no tiene email
        if not email:
            raise ValueError('el usuario debe tener un email')
        if not username:
            raise ValueError('el usuario debe tener un username')
        
        user= self.model(
            
            email=self.normalize_email(email),
            username=username,  
            first_name =first_name,
            last_name=last_name
            
        )
        user.set_password(password)
    #se llama para guardar la transaccion en la bd
        user.save(using=self._db)
        return user

    #funcion que permite crear super usuario
    def  create_superuser(self,first_name,last_name,username,email,password):
        user =self.create_user (            
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name            
        )
        user.is_admin = True
        user.is_active=True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username= models.CharField(max_length=128, unique=True)
    email= models.CharField(max_length=100, unique=True)
    phone= models.CharField(max_length=50)
    
    
#campos atributos propio de Django 
    date_joined= models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD= 'email' # cambia la forma de logeo por defecto 
    
    #cmapos obligatorios, si es el correo de la empresa 
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    #se instancia para ser utlizado en esta clase
    objects = MyAccontManager()
    
    
    def __str__(self):
        return self.email
    
    #funcion de permisos
    def has_perm(self, perm,obj=None):
        return self.is_admin #solo si es administrado puede modificar 
    
    #funcion de modulos
    
    def has_module_perms (self, add_label):
        return True

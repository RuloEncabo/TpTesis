from datetime import date
#from . models import UsuarioChofer,Usuario, TipoKilometro 
from django.db import models
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from usuarios.models import Usuario
from usuarios.models import UsuarioChofer
from chofer.models import Chofer

class TipoKilometros(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Movimientos(models.Model):
    mov_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, blank=True)
    nFlota = models.CharField(max_length=60, null=True, blank=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField(null=True, blank=True)
    kmInicio = models.IntegerField(default=0)
    kmFin = models.IntegerField(null=True, blank=True)
    lugar_inicio = models.CharField(max_length=60)
    lugar_fin = models.CharField(max_length=60, null=True, blank=True)
    tipo_kilometro = models.ForeignKey('TipoKilometro.TipoKilometro', on_delete=models.CASCADE)
    lleva_carga = models.BooleanField(default=False)
    permanencia = models.BooleanField(default=False)
    diasPermanencia = models.IntegerField(default=0)
    cruce_frontera = models.BooleanField(default=False)
    #active = models.BooleanField(default=False)
    modif = models.DateTimeField(auto_now=True)
    comentarios = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha y hora de la última actualización
    
    @property
    def diferencia_km(self):
        if self.kmFin is not None and self.kmInicio is not None:
            return self.kmFin - self.kmInicio
        return None
    

    def __str__(self):
        return f'{self.usuario_id} - {self.inicio} a {self.fin}'
    
    """ 
    
    def __str__(self):
        return f"Movimiento {self.mov_id} - {self.chofer}"
    

    def clean(self):
        # Verificar que kmFin sea mayor que kmInicio
        if self.kmFin is not None and self.kmFin < self.kmInicio:
            raise ValidationError('kmFin debe ser mayor que kmInicio')

        # Verificar si el chofer tiene un movimiento sin cerrar
        #  if not self.fin:
        #     if Movimientos.objects.filter(chofer=self.chofer, fin__isnull=True).exclude(pk=self.pk).exists():
        #        raise ValidationError('El chofer tiene un movimiento sin cerrar.')

        # Verificar que lugar_inicio no se pueda modificar si hay un movimiento sin cerrar
        ultimo_movimiento = Movimientos.objects.filter(chofer=self.chofer).order_by('-inicio').first()
        if ultimo_movimiento and not ultimo_movimiento.fin and self.lugar_inicio != ultimo_movimiento.lugar_inicio:
            raise ValidationError('No se puede modificar el campo lugar_inicio mientras haya un movimiento sin cerrar.')
    
    
   
        # Verificar que haya un viaje activo
        viaje_activo = Viaje.objects.filter(chofer=self.chofer, activo=True).exists()
        if not viaje_activo:
            raise ValidationError('No hay un viaje activo para registrar el movimiento.')
            
            """
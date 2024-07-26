from datetime import date
#from .models import UsuarioChofer, TipoKilometro 
from django.db import models
from django.conf import settings
from django.db import models
from django.forms import ValidationError

class Movimiento(models.Model):
    mov_id = models.AutoField(primary_key=True)
    chofer = models.OneToOneField('usuarios.UsuarioChofer', on_delete=models.CASCADE)
    #viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    nFlota = models.CharField(max_length=60, null=True, blank=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField(null=True, blank=True)
    kmInicio = models.IntegerField(default=0)
    kmFin = models.IntegerField(null=True, blank=True)
    lugar_inicio = models.CharField(max_length=60)
    lugar_fin = models.CharField(max_length=60, null=True, blank=True)
    tipo_kilometro = models.ForeignKey('TipoKilometro', on_delete=models.CASCADE)
    lleva_carga = models.BooleanField(default=False)
    permanencia = models.BooleanField(default=False)
    diasPermanencia = models.IntegerField(default=0)
    cruce_frontera = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    modif = models.DateTimeField(auto_now=True)
    comentarios = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.mov_id)
    
    def clean(self):
        # Verificar que kmFin sea mayor que kmInicio
        if self.kmFin is not None and self.kmFin < self.kmInicio:
            raise ValidationError('kmFin debe ser mayor que kmInicio')

        # Verificar si el chofer tiene un movimiento sin cerrar
        if not self.fin:
            if Movimiento.objects.filter(chofer=self.chofer, fin__isnull=True).exclude(pk=self.pk).exists():
                raise ValidationError('El chofer tiene un movimiento sin cerrar.')

        # Verificar que lugar_inicio no se pueda modificar si hay un movimiento sin cerrar
        ultimo_movimiento = Movimiento.objects.filter(chofer=self.chofer).order_by('-inicio').first()
        if ultimo_movimiento and not ultimo_movimiento.fin and self.lugar_inicio != ultimo_movimiento.lugar_inicio:
            raise ValidationError('No se puede modificar el campo lugar_inicio mientras haya un movimiento sin cerrar.')
    
    
    """ 
        # Verificar que haya un viaje activo
        viaje_activo = Viaje.objects.filter(chofer=self.chofer, activo=True).exists()
        if not viaje_activo:
            raise ValidationError('No hay un viaje activo para registrar el movimiento.')
            
            """
from datetime import date
from django.db import models
from django.conf import settings

from django.db import models

class Movimiento(models.Model):
    
    mov_id = models.AutoField(primary_key=True)
    chofer = models.ForeignKey('chofer.Chofer', on_delete=models.CASCADE)
    nFlota = models.CharField(max_length=60, null=True, blank=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField(null=True, blank=True)
    kmInicio = models.IntegerField(default=0)
    kmFin = models.IntegerField(null=True, blank=True)
    lugar_inicio = models.CharField(max_length=60)
    lugar_fin = models.CharField(max_length=60, null=True, blank=True)
   # tipo_kilometro = models.ForeignKey(TipoKilometro, on_delete=models.CASCADE)
    lleva_carga = models.BooleanField(default=False)
    permanencia = models.BooleanField(default=False)
    diasPermanencia = models.IntegerField(default=0)
    cruce_frontera = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    modif = models.DateTimeField(auto_now=True)
    comentarios = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.mov_id)
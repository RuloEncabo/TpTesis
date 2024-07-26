from django.db import models
from django.contrib.auth.models import User
from usuarios.models import UsuarioChofer

class Viaje(models.Model):
    chofer = models.ForeignKey(UsuarioChofer, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fin = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Viaje {self.pk} - Chofer: {self.chofer.usuario.first_name} {self.chofer.usuario.last_name}"
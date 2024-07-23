from django.db import models

class Movimiento(models.Model):
    # Definición del modelo Movimiento (asumiendo que ya está definido)
    mov_id = models.AutoField(primary_key=True)
    #tipo_kilometro = models.ForeignKey('TipoKilometro', on_delete=models.CASCADE, related_name='movimiento', null=True, blank=True)

    def __str__(self):
        return str(self.mov_id)  # O el campo que desees usar como representación

class TipoKilometro(models.Model):
    tk_nombre = models.CharField(max_length=60, blank=True, null=True)
    
    def __str__(self):
        return self.tk_nombre

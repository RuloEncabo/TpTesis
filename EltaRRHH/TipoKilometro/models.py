from django.db import models


class TipoKilometro(models.Model):
    idTipoKilometro = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.descripcion

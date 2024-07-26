from django.contrib import admin
from .models import TipoKilometro
from django.utils.html import format_html


class TipoKmAdim(admin.ModelAdmin):
    #lo que muestra en la tabla de usuarios 
    list_display = ('idTipoKilometro','descripcion')



# Register your models here.
admin.site.register(TipoKilometro, TipoKmAdim)
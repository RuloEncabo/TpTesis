from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Chofer
from django.utils.html import format_html

# Register your models here.
class ChoferAdmin(admin.ModelAdmin):
    #control que permita adinistrar mis imagenes
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;" >'.format(object.foto.url))
    
    thumbnail.short_description = 'Imagen de Perfil'
    list_display =('thumbnail' , 'usuario', 'dni', 'direccion', 'localidad', 'provincia', 'ingresoFCA_venc', 'licencia_venc','psicofisico_venc', 'curso_venc')

admin.site.register(Chofer, ChoferAdmin)
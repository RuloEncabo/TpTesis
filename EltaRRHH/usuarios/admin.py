from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, UsuarioChofer
from django.utils.html import format_html


class Accontadmin(UserAdmin):
    #lo que muestra en la tabla de usuarios 
    list_display = ('email','first_name','last_name', 'last_login','date_joined','is_active')
    # cuando seleciones una celda. da el detalle de una usuario 
    list_display_link = ('email','first_name','last_name')
    #campos de lectura
    readonly_fields = ('date_joined','last_login')
    #se muestra ordenado por fecha ascendente
    ordering = ('-date_joined',)
    
    #inicializar Filtros
    filter_horizontal=()
    list_filter=()
    fieldsets=()


class UsuarioChoferAdmin(admin.ModelAdmin):
    #control que permita adinistrar mis imagenes
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;" >'.format(object.foto.url))
    
    thumbnail.short_description = 'Imagen de Perfil'
    list_display =('thumbnail' , 'usuario', 'dni', 'direccion', 'localidad', 'provincia', 'ingresoFCA_venc', 'licencia_venc','psicofisico_venc', 'curso_venc')
    
    
# Register your models here.
admin.site.register(Usuario, Accontadmin)
admin.site.register(UsuarioChofer, UsuarioChoferAdmin)
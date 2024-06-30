from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class Accontadmin(UserAdmin):
    #lo que muestra en la tabla de usuarios 
    list_display = ('email','first_name','last_name', 'username','last_login','date_joined','is_active')
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


# Register your models here.
admin.site.register(Usuario, Accontadmin)
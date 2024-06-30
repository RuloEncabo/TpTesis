from django.contrib import admin
from .models import Chofer
# Register your models here.

class ChoferAdmin (admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido','dni','movil')
    prepopulated_fields = {'slug': ('apellido',)}
    search_fields = ['nombre']

#registar la entidad

admin.site.register (Chofer, ChoferAdmin)
    

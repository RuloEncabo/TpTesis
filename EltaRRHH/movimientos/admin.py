from django.contrib import admin
from .models import Movimientos

# Register your models here.
class movimentosAdmin(admin.ModelAdmin):
    
    
    list_display =('chofer' , 'nFlota', 'inicio', 'kmInicio', 'lugar_inicio', 'tipo_kilometro', 'fin', 'kmFin',
                    'lugar_fin', 'permanencia', 'diasPermanencia', 'cruce_frontera', 'comentarios', 'created_at')
    
    
# Register your models here.
admin.site.register(Movimientos, movimentosAdmin)
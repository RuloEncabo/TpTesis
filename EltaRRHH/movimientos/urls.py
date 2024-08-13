from django.urls import path
from . import views

urlpatterns = [
    path('registrarmovimiento/', views.registrarmovimiento, name='registrarmovimiento'),
    path('registrarmovimientoc/', views.registrarmovimientoc, name='registrarmovimientoc'),
    path('inicioMov/', views.inicioMov, name='inicioMov'),
    path('finMov/<int:mov_id>/', views.finMov, name='finMov'),
    path('modificarmovimiento/<int:mov_id>/', views.modificarmovimiento, name='modificarmovimiento'),
    path('borrarmovimiento/', views.borrarmovimiento, name='borrarmovimiento'),
    path('listmovimiento/', views.listmovimiento, name='listmovimiento'),
    path('movimiento/', views.movimiento, name='movimiento'),
    path('movchofer/', views.movchofer, name='movchofer'),
    path('listmovimientoChofer/', views.listmovimientoChofer, name='listmovimientoChofer'),
    path('kpi/', views.kpi, name='kpi'),
]
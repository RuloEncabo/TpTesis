from django.urls import path
from . import views

urlpatterns = [
    path('registrarmovimiento/', views.registrarmovimiento, name='registrarmovimiento'),
    path('registrarmovimientoc/', views.registrarmovimientoc, name='registrarmovimientoc'),
    path('listmovimiento/', views.listmovimiento, name='listmovimiento'),
    path('movimiento/', views.movimiento, name='movimiento'),
    path('movimientoc/', views.movimientoc, name='movimientoc'),
    path('listmovimientoChofer/', views.listmovimientoChofer, name='listmovimientoChofer'),
    path('kpi/', views.kpi, name='kpi'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('registrarmovimiento/', views.registrarmovimiento, name='registrarmovimiento'),
    path('registrarmovimientoc/', views.registrarmovimientoc, name='registrarmovimientoc'),
    path('listmovimiento/', views.listmovimiento, name='listmovimiento'),
    path('movimiento/', views.movimiento, name='movimiento'),
    path('movchofer/', views.movchofer, name='movchofer'),
    path('listmovimientoChofer/', views.listmovimientoChofer, name='listmovimientoChofer'),
    path('kpi/', views.kpi, name='kpi'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('registrarmovimiento/', views.registrarmovimiento, name='registrarmovimiento'),
    path('listmovimiento/', views.listmovimiento, name='listmovimiento'),
    path('movimiento/', views.movimiento, name='movimiento'),
    path('listmovimientoChofer/', views.listmovimientoChofer, name='listmovimientoChofer'),
    path('analitica/', views.analitica, name='analitica'),
]
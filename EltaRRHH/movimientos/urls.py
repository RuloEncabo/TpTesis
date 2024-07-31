from django.urls import path
from . import views

urlpatterns = [
    path('registrarmovimiento/', views.registrarmovimiento, name='registrarmovimiento'),
    path('listmovimiento/', views.listmovimiento, name='listmovimiento'),
    path('movimiento/', views.movimiento, name='movimiento'),
]
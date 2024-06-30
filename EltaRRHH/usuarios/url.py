from django.urls import path
from . import views

urlpatterns =[
    
    path('register/', views.register, name = 'register'), # definicion de funciones registar
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'salir'),
    
]
from django.urls import path
from. import views

urlpatterns = [
    
    path('registro/', views.registro, name='registro'),     #funcion def que registra un usuario
    path('login/', views.registro, name='login'),
    path('logout/', views.registro, name='logout'),
    
]
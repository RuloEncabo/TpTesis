from django.urls import path
from. import views

urlpatterns = [
    
    path('registro/', views.registro, name='registro'),     #funcion def que registra un usuario
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
]
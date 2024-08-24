from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import (
    CustomPasswordResetView, 
    CustomPasswordResetDoneView, 
    CustomPasswordResetConfirmView, 
    CustomPasswordResetCompleteView
)

urlpatterns = [
    
    path('home/', views.home, name='home'),
    path('registro/', views.registro, name='registro'),     #funcion def que registra un usuario
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('listar/', views.listar, name='listar'),
    #path('admin/', views.home, name='admin'),
    path('chofer/', views.chofer, name='chofer'),
    path('listusuario/', views.listusuario, name='listusuario'),
    path('listusuariochofer/', views.listusuariochofer, name='listusuariochofer'),
    path('', views.home, name='home'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'), # ruta para la funcion activate con los parametros  
    path('delete_usuario/', views.delete_usuario, name='delete_usuario'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
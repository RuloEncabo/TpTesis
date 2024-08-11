from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home, name='home'),
    path('registro/', views.registro, name='registro'),     #funcion def que registra un usuario
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sol_reset_pass/',views.sol_reset_pass, name='sol_reset_pass'),
    path('listar/', views.listar, name='listar'),
    #path('admin/', views.home, name='admin'),
    path('chofer/', views.chofer, name='chofer'),
    path('listusuario/', views.listusuario, name='listusuario'),
    path('listusuariochofer/', views.listusuariochofer, name='listusuariochofer'),
    path('', views.home, name='home'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'), # ruta para la funcion activate con los parametros  
    path('delete_usuario/', views.delete_usuario, name='delete_usuario'),
    path('pedidocuenta/', views.pedidocuenta, name='pedidocuenta'),
    
    
]
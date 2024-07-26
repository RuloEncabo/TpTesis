from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrarviaje, name='registrarviaje'),
    
]
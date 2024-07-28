from django.urls import path
from . import views

urlpatterns = [
    path('registrarkm/', views.registrarkm, name='registrarkm'),
    
]
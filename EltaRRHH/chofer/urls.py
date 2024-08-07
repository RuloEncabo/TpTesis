from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('listchofer/', views.listchofer, name='listchofer'),
    path('listdoc/', views.listdoc, name='listdoc'),
    #path('modidoc/', views.modidoc, name='modidoc'),
    path('modidoc/<int:chofer_id>/', views.modidoc, name='modidoc'),
    path('Borrarchofer/', views.Borrarchofer, name='Borrarchofer'),
    #path('editarchofer/', views.editarchofer, name='editarchofer'),
    path('editarchofer/<int:chofer_id>/', views.editarchofer, name='editarchofer'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
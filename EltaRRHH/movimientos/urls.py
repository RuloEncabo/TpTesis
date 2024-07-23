from django.urls import path
from .views import MovimientoCreateView, MovimientoListView, MovimientoUpdateView, MovimientoDeleteView

urlpatterns = [
    path('movimiento/create/', MovimientoCreateView.as_view(), name='movimiento-create'),
    path('movimiento/', MovimientoListView.as_view(), name='movimiento-list'),
    path('movimiento/<int:pk>/edit/', MovimientoUpdateView.as_view(), name='movimiento-update'),
    path('movimiento/<int:pk>/delete/', MovimientoDeleteView.as_view(), name='movimiento-delete'),
]
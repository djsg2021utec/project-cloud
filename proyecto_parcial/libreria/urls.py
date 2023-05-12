from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('almacen', views.almacen, name='almacen'),
    path('almacen/crear', views.crear_producto, name='crear_producto'),
]
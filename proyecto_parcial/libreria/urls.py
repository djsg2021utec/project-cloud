from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('almacen/', views.almacen, name='almacen'),
    path('compras/', views.compras, name='compras'),
    path('ventas/', views.ventas, name='ventas'),

    path('almacen/crear', views.crear_producto, name='crear_producto'),
    path('compras/crear', views.crear_compra, name='crear_compra'),
    path('ventas/crear', views.crear_venta, name='crear_venta'),

    path('almacen/<int:id>/borrar',views.borrar_producto, name='borrar_producto'),
    path('compras/<int:id>/borrar',views.borrar_compra, name='borrar_compra'),
    path('ventas/<int:id>/borrar',views.borrar_venta, name='borrar_venta')
]

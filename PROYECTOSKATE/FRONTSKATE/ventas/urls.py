from django.urls import path, include
from . import views
from django.conf.urls import include
from .views import administrador_view   # importando la vista


urlpatterns = [

    path('',views.index, name="index"),
    path('compras',views.compras),
    path('administrador',views.administrador),
    path('empleados',views.empleados),
    path('clientes',views.clientes),
    path('adminProd',views.adminProd),
    path('sucursal',views.sucursal),
    path('proveedores',views.proveedores),


    path('administrador/',administrador_view, name='administrador'), # configurando la urls.


    path('catalogo', views.catalogo, name='post_list'),
    path('catalogo_login', views.catalogo_login, name='post_list'),



    path('galeria_html', views.galeria_html, name='post_list'),

    path('login', views.login, name='post_list'),


]
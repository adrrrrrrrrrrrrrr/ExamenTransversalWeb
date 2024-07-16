
from django.contrib import admin
from django.urls import path
from venta import views

from django.conf import settings
from django.conf.urls.static import static

from . import views_load
from . import views_restfull



urlpatterns = [

    path('empleado1', views.empleado),
    path('empleado', views.EmpleadoList.as_view()),
    path('empleado/<int:pk>', views.EmpleadoDetail.as_view()),

    path('cliente1', views.cliente),
    path('cliente', views.ClienteList.as_view()),
    path('cliente/<int:pk>', views.ClienteDetail.as_view()),

    path('producto1', views.producto),
    path('producto', views.ProductoList.as_view()),
    path('producto/<int:pk>', views.ProductoDetail.as_view()),


    path('sucursal1', views.sucursal),
    path('sucursal', views.SucursalList.as_view()),
    path('sucursal/<int:pk>', views.SucursalDetail.as_view()),

    path('proveedores1', views.proveedores),
    path('proveedores', views.ProveedoresList.as_view()),
    path('proveedores/<int:pk>', views.ProveedoresDetail.as_view()),

    path('backend/productos/',  views.ProductosList.as_view()),
    path('backend/productos_login/',  views.ProductosListLogin.as_view()),


    path('load/', views_load.LoadData.as_view()),

    #path('restfull/region/', views_restfull.rf_region),  
    #path('restfull/region/<int:cod_region>', views_restfull.rf_region_pk),
    #path('restfull/region_load', views_restfull.rf_load_region),
] 




from rest_framework import serializers
from .models import *


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id_empleado', 'rut','nombre', 'apaterno', 'amaterno', 'correo', 'numero_telefono', 'sexo', 'Fec_nacimiento', 'edad', 'direccion')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id_cliente', 'rut','nombre', 'apaterno', 'amaterno', 'correo', 'numero_telefono', 'sexo', 'Fec_nacimiento', 'edad', 'direccion')


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('sku', 'descripcion','color', 'marca', 'stock')


class ViewProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('idProd','imagen','imagen_sb','nombre','desc_corta','cant_favoritos','cant_vistos','precio')



class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id_sucursal', 'nombre_sucursal','direccion')



class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ('id_proveedor', 'nombre_proveedor','direccion','telefono','correo')




from django.db import models

# Create your models here.


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    Fec_nacimiento = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)


    
    class Meta:
        db_table = 'adrian_empleado'




class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    Fec_nacimiento = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)


    
    class Meta:
        db_table = 'adrian_cliente'



class Producto(models.Model):
    sku = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)

    
    class Meta:
        db_table = 'adrian_producto'





#################################################################################################################


class Productos(models.Model):
    idProd =models.AutoField(primary_key=True)
    imagen = models.CharField(max_length=100)
    imagen_sb = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    desc_corta = models.CharField(max_length=100)
    cant_favoritos = models.IntegerField(blank=True, null=True)  
    cant_vistos = models.IntegerField(blank=True, null=True)  
    precio = models.IntegerField(blank=True, null=True)  
    class Meta:
    	db_table = 'adrian_productos'


#################################################################################################################

class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    
    

    
    class Meta:
        db_table = 'adrian_sucursal'


class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

    
    class Meta:
        db_table = 'adrian_proveedores'

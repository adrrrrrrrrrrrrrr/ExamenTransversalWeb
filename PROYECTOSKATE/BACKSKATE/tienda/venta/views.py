from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import Http404

from .models import *
from .serializers import *


from rest_framework.permissions import IsAuthenticated

# Create your views here.

class JSONResponseOkRows(HttpResponse):
    def __init__(self, data,msg, **kwargs):
        #print(len(data))
        data= {"OK":True,"count":len(data),"registro":data,"msg":msg}
        #print("data",data)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOkRows, self).__init__(content, **kwargs)


class JSONResponseOk(HttpResponse):
    def __init__(self, data, msg,**kwargs):
        #print("data",data)
        data= {"OK":True,"count":"1","registro":data,"msg":msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOk, self).__init__(content, **kwargs)

class JSONResponseErr(HttpResponse):
    def __init__(self, data, **kwargs):
        data= {"OK":False,"count":"0","msg":data}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseErr, self).__init__(content, **kwargs)








#######################################################################

def empleado(request):
    registro = Empleado.objects.all()
    print("Registro",registro)
    serializer = EmpleadoSerializer(registro, many=True)
    #return HttpResponse("adadadada")
    return JSONResponseOkRows(serializer.data,"")

class EmpleadoList(APIView):
    def get(self, request, format=None):
         registro = Empleado.objects.all()
         serializer = EmpleadoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = EmpleadoSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
class EmpleadoDetail(APIView):
    def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = EmpleadoSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = EmpleadoSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#######################################################################


def cliente(request):
    registro = Cliente.objects.all()
    print("Registro",registro)
    serializer = ClienteSerializer(registro, many=True)
    #return HttpResponse("adadadada")
    return JSONResponseOkRows(serializer.data,"")

class ClienteList(APIView):
    def get(self, request, format=None):
         registro = Cliente.objects.all()
         serializer = ClienteSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = ClienteSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
class ClienteDetail(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = ClienteSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = ClienteSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    





#######################################################################


def producto(request):
    registro = Producto.objects.all()
    print("Registro",registro)
    serializer = ProductoSerializer(registro, many=True)
    #return HttpResponse("adadadada")
    return JSONResponseOkRows(serializer.data,"")

class ProductoList(APIView):
    def get(self, request, format=None):
         registro = Producto.objects.all()
         serializer = ProductoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = ProductoSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
class ProductoDetail(APIView):
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = ProductoSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = ProductoSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


#####################################################################


class ProductosList(APIView):
    def get(self, request, format=None):
         registro = Productos.objects.all()
         serializer = ViewProductosSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")    
    


#####################################################################



class ProductosListLogin(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
         registro = Productos.objects.all()
         serializer = ViewProductosSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    


#####################################################################


def sucursal(request):
    registro = Sucursal.objects.all()
    print("Registro",registro)
    serializer = SucursalSerializer(registro, many=True)
    #return HttpResponse("adadadada")
    return JSONResponseOkRows(serializer.data,"")

class SucursalList(APIView):
    def get(self, request, format=None):
         registro = Sucursal.objects.all()
         serializer = SucursalSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = SucursalSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
class SucursalDetail(APIView):
    def get_object(self, pk):
        try:
            return Sucursal.objects.get(pk=pk)
        except Sucursal.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = SucursalSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = SucursalSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



#######################################################################

def proveedores(request):
    registro = Proveedores.objects.all()
    print("Registro",registro)
    serializer = ProveedoresSerializer(registro, many=True)
    #return HttpResponse("adadadada")
    return JSONResponseOkRows(serializer.data,"")

class ProveedoresList(APIView):
    def get(self, request, format=None):
         registro = Proveedores.objects.all()
         serializer = ProveedoresSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = ProveedoresSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
class ProveedoresDetail(APIView):
    def get_object(self, pk):
        try:
            return Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = ProveedoresSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = ProveedoresSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
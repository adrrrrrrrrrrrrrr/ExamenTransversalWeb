from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # esto es necesario para definir la vista



# Create your views here.


TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR, "templates"),'


}
   
def index(request):
    return render(request, "index.html")



def compras(request):
    return render(request, "compras.html")



def administrador(request):
    return render(request, "administrador.html")


def empleados(request):
    return render(request, "empleados.html")

def clientes(request):
    return render(request, "clientes.html")


def adminProd(request):
    return render(request, "adminProd.html")

def sucursal(request):
    return render(request, "sucursal.html")


def proveedores(request):
    return render(request, "proveedores.html")


@login_required
def administrador_view(request):                          # protegiendo la vista
    return render(request, 'administrador.html')



#######################################

def galeria_html(request):
    html = "<html><body>Galeria Html</body></html>"
    return HttpResponse(html)

def catalogo(request):
    return render(request, 'catalogo.html')



def login(request):
    return render(request, 'login.html')


def catalogo_login(request):
    return render(request, 'catalogo_login.html')
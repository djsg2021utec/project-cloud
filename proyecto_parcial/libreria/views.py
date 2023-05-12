from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html')


def almacen(request):
    return render(request,'almacen/index.html')
def crear_producto(request):
    return render(request,'almacen/crear.html')
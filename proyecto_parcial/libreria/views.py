from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import View
from libreria.models import Almacen, Compra
import requests
from .forms import AlmacenForm, CompraForm, VentaForm

#from.models import Producto

# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html')


def almacen(request):
    #productos = Almacen.objects.all()
    r = requests.get('http://54.236.217.38:9003/products')
    productos = r.json()
    return render(request,'almacen/index.html',{'Productos':productos})

def crear_producto(request):
    formulario = AlmacenForm(request.POST or None)
    if formulario.is_valid():
        x = requests.post('http://54.236.217.38:9003/products', data = request.POST)
        return HttpResponseRedirect(reverse('almacen'))
    return render(request,'almacen/crear.html',{'formulario':formulario})

def borrar_producto(request,id=0):
    x = requests.delete('http://54.236.217.38:9003/product/'+str(id))
    return HttpResponseRedirect(reverse('almacen'))

def compras(request):
    r = requests.get('http://54.236.217.38:9001/compras')
    regcompras = r.json()
    return render(request,'compras/index.html',{'Regcompras':regcompras})

def crear_compra(request):
    formulario = CompraForm(request.POST or None)
    if formulario.is_valid():
        x = requests.post('http://54.236.217.38:9001/compras', data = request.POST)
        return HttpResponseRedirect(reverse('compras'))
    return render(request,'compras/crear.html',{'formulario':formulario})

def borrar_compra(request,id=0):
    x = requests.delete('http://54.236.217.38:9001/compra/'+str(id))
    return HttpResponseRedirect(reverse('compras'))



def ventas(request):
    r = requests.get('http://54.236.217.38:9002/ventas')
    regventas = r.json()
    return render(request,'ventas/index.html',{'Regventas':regventas})

def crear_venta(request):
    formulario = VentaForm(request.POST or None)
    if formulario.is_valid():
        x = requests.post('http://54.236.217.38:9002/ventas', data = request.POST)
        return HttpResponseRedirect(reverse('ventas'))
    return render(request,'ventas/crear.html',{'formulario':formulario})

def borrar_venta(request,id=0):
    x = requests.delete('http://54.236.217.38:9002/venta/'+str(id))
    return HttpResponseRedirect(reverse('ventas'))


def editar_producto(request):
    return render(request,'almacen/editar.html')

class AlmacenView(View):

    def get(self,request):
        
        productos = list(Almacen.objects.values())
        if len(productos)>0:
            datos={'message': 'Success','productos':productos}
        else:
            datos={'message': 'Products not found'}
        return JsonResponse(datos)

    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass

    
    
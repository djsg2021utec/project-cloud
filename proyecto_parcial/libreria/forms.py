from django import forms
from .models import Almacen, Compra, Venta

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = '__all__'


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
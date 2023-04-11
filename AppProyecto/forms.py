from django import forms

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    DNI=forms.CharField()
    email=forms.EmailField()

class ProveedorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    CUIT=forms.CharField(max_length=13)
    email=forms.EmailField()
    condicion_pago=forms.CharField(max_length=20)

class ProductoForm(forms.Form):
    descripcion=forms.CharField(max_length=50)
    marca=forms.CharField(max_length=50)
    unidad_de_medida=forms.CharField(max_length=50)
    precio=forms.FloatField()


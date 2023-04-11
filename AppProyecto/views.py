from django.shortcuts import render
from .models import Cliente, Proveedor, Producto
from .forms import ClienteForm, ProveedorForm, ProductoForm
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenido a la página principal")

def inicioApp(request):
    return render(request, "AppProyecto/inicio.html")

def clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente()
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            cliente.DNI = form.cleaned_data['DNI']
            cliente.email = form.cleaned_data['email']
            cliente.save()
            form  = ClienteForm()
    else:
        form = ClienteForm()


    clientes = Cliente.objects.all()
    context={"clientes":clientes, "form":form}
    return render(request, "AppProyecto/clientes.html",context)

def proveedores(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = Proveedor()
            proveedor.nombre = form.cleaned_data['nombre']
            proveedor.apellido = form.cleaned_data['apellido']
            proveedor.CUIT = form.cleaned_data['CUIT']
            proveedor.email = form.cleaned_data['email']
            proveedor.condicion_pago = form.cleaned_data['condicion_pago']
            proveedor.save()
            form  = ProveedorForm()
    else:
        form = ProveedorForm()


    proveedores = Proveedor.objects.all()
    context={"proveedores":proveedores, "form":form}
    return render(request, "AppProyecto/proveedores.html",context)

def productos(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = Producto()
            producto.descripcion = form.cleaned_data['descripcion']
            producto.marca = form.cleaned_data['marca']
            producto.unidad_de_medida = form.cleaned_data['unidad_de_medida']
            producto.precio = form.cleaned_data['precio']
            producto.save()
            form  = ProductoForm()
    else:
        form = ProductoForm()


    productos = Producto.objects.all()
    context={"productos":productos, "form":form}
    return render(request, "AppProyecto/productos.html",context)

def busqueda_marca(request):
    return render(request, "AppProyecto/busqueda_marca.html")

def buscar(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        productos = Producto.objects.filter(marca__icontains=marca)
        return render(request, "AppProyecto/resultadosBusqueda.html", {"productos":productos,"marca":marca})
    else:
        respuesta = "Sin datos"
    return HttpResponse(respuesta)


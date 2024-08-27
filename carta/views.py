from django.shortcuts import render
from .models import Product

# Create your views here.
# request -> response

def home(request):
    return render(request, "home.html")

def carta(request):
    # Hacer llamados a una base de datos
    #emails los clientes
    #...
    productos = Product.objects.all()
    
    return render(request, "carta.html", {"productos": productos})

def ubicaciones(request):
    return render(request, "ubicaciones.html")
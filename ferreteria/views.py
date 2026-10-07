from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    # Consulta a la base de datos usando el ORM
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'productos/lista.html', {'productos': productos})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Producto, Categoria

# 1. Landing Page + Catálogo (Pública)
def home(request):
    productos = Producto.objects.select_related('categoria').all()
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {
        'productos': productos,
        'categorias': categorias
    })

# 2. Registro de Usuario (Pública)
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada exitosamente para {username}. ¡Ahora puedes iniciar sesión!')
            return redirect('login')  # Redirige a la pantalla de login tras registrarse
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

# 3. Lógica del Carrito (Requiere Autenticación)
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))

    if cantidad > producto.stock:
        messages.error(request, f"No hay suficiente stock disponible ({producto.stock} unidades).")
        return redirect('home')

    carrito = request.session.get('carrito', {})
    str_id = str(producto_id)

    if str_id in carrito:
        nueva_cantidad = carrito[str_id]['cantidad'] + cantidad
        if nueva_cantidad > producto.stock:
            messages.error(request, f"Excedes el stock disponible ({producto.stock} unidades).")
            return redirect('ver_carrito')
        carrito[str_id]['cantidad'] = nueva_cantidad
    else:
        carrito[str_id] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': cantidad,
            'imagen': producto.imagen or ''
        }

    request.session['carrito'] = carrito
    messages.success(request, f"Se agregó '{producto.nombre}' al carrito.")
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

@login_required
def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    str_id = str(producto_id)
    if str_id in carrito:
        del carrito[str_id]
        request.session['carrito'] = carrito
        messages.info(request, "Producto eliminado del carrito.")
    return redirect('ver_carrito')

@login_required
def procesar_compra(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.warning(request, "El carrito está vacío.")
        return redirect('home')

    # Verificar stock
    for item_id, item_data in carrito.items():
        producto = get_object_or_404(Producto, pk=item_id)
        if producto.stock < item_data['cantidad']:
            messages.error(request, f"Stock insuficiente para {producto.nombre}.")
            return redirect('ver_carrito')

    # Descontar stock
    for item_id, item_data in carrito.items():
        producto = Producto.objects.get(pk=item_id)
        producto.stock -= item_data['cantidad']
        producto.save()

    # Vaciar carrito
    request.session['carrito'] = {}
    messages.success(request, "¡Compra realizada con éxito! El stock ha sido actualizado.")
    return redirect('home')
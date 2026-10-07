from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # list_display muestra 4 campos (cumple con el mínimo de 3)
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    # Búsqueda por nombre de producto y por el nombre de la categoría asociada
    search_fields = ('nombre', 'categoria__nombre')
    # Filtro lateral por categoría
    list_filter = ('categoria',)
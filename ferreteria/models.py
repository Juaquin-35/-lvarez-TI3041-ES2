from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    stock = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    imagen = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nombre
# Anexo: Declaración de Uso de Inteligencia Artificial
-Herramienta utilizada: Gemini (Google DeepMind)

* **Prompt de entrada**
    *nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    categoria = models.CharField(max_length=50, verbose_name="Categoría")
    precio = models.IntegerField(verbose_name="Precio (CLP)")
    stock = models.IntegerField(verbose_name="Stock disponible")
    def __str__(self):
    return f"{self.nombre} ({self.categoria})"

    al modelo le podria implementar imagenes?*

* **Respuesta / Solución aplicada**
    Ayudo con la corrección e implementación para las imagenes que podria agregar mas adelante reutilizando codigo
    del anterior proyecto.


* **Prompt de entrada**
    *estoy intentando corroborar el inicio de mi proyecto mediante esto py manage.py runserver pero no inicia*

* **Respuesta / Solución aplicada**
    El problema de no inicar resulto en un simple error de una libreria faltante que seria la de Pillow
    que sirve para la implementación de imagenes.


* **Prompt de entrada**
    *
        •      Cree el superusuario y verifique acceso a /admin.

        •      Registre el modelo en admin.py con list_display (3

        campos o más) y search_fields o list_filter.

        •      Cree, edite y elimine un registro de prueba desde

        /admin para verificar la gestión del contenido. Commit etapa-2-admin. 
    *
    *
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
    *
* **Respuesta / Solución aplicada**
    se le entrego parte de la instrucción dando como resultado el codigo del apartado de admin corroborando el correcto acceso y la legibilidad de los datos dentro de esta misma.


* **Prompt de entrada**
    *
    Etapa 3: Poblamiento con IA y listado desde la
    BD
    •      Poblamiento con IA (obligatorio): solicite a la
    IA los datos de su variante (volumen completo, datos realistas en español) como
    fixture JSON de Django o script de poblamiento con el ORM. Cargue los datos
    (loaddata o ejecutando el script) y verifíquelos en /admin.
    •      Reemplace la lista estática de la ES1: el template
    principal ahora muestra el listado consultando la BD con el ORM. Queda
    prohibido mantener datos en duro en vistas o templates.
    •      Commit etapa-3-bd. 
    *

    *
    y que hay de estos productos que tenia guardados pero pasandolos al formato correspondiente para lograr esos objetivos
    *

* **Respuesta / Solución aplicada**
    se le entrego los requisitos necesarios para la generación del poblamiento de datos y a su vez al terminar la entrega de los datos y correspondientes codigos se le entrego otro prompt en donde se le entrega una lista de datos(productos) que fue utilizada anteriormente para ser reconstruida de acorde al modelo a utilizar, al igual que la implementación del siguiente codigo para consultar directamente a la base de datos sobre los productos ya implementados.

    *
    from django.shortcuts import render
    from .models import Producto

    def lista_productos(request):
        # Consulta a la base de datos usando el ORM
        productos = Producto.objects.select_related('categoria').all()
        return render(request, 'productos/lista.html', {'productos': productos})
        *


* **Prompt de entrada**
    *
    bien lo que necesito es que se puedan ver los productos com si fuera un catalogo ya que no tiene nada de front end pero principalmente quiero que sea como un Landing page en el cual tenga las respectivas opciones de una ferreteria sobre nosotros la ubicacion, el catalogo, etc claro tambien que para el catalogo tenga un carrito de compra en el cual pueda agregar los productos que quiero comprar y poder seleccionar la cantidad que quiero comprar de ese producto y ya en el carrito de compra ejecutar la compra la cual disminuiria la cantidad del producto es decir su stock y que solo se pueda comprar con un usuario o administrador ademas de implementar un panel de administrador respectivo al cual solo los administradores creados mediante creatersuperuser solo pueda acceder implementando la opcion de registro y inicio de sesion para poder usar el carrito de compra. 
    *

* **Respuesta / Solución aplicada**
    Se le entrego prompt para terminar y dejar pulida la parte completa de Front-End entregando los respectivos codigos referente a las templates para la legibilidad de los datos tanto para usuarios y administradores dejando el panel de Admin a parte solo para SuperUsuarios, al igual que la implementación del carrito de compras el desconteo de stock funcional y el bloqueo de un producto que se quede sin stock.


* **Prompt de entrada**
    *
    hice todos los respectivos cambios pero cuando lo inicio no muestra nada da el error de que no existe
    *
    *
    bien necesito solucionar el url de

    path('registro/', views.registro, name='registro'),
    *

* **Respuesta / Solución aplicada**
    Al intentar iniciar el proyecto daba como resultado el simple error de la mal implementación de las urls al igual que se soluciono un problema relacionado con login y registro ya que sus respectivas templates aun no estaban creadas.


* **Prompt de entrada**
    *
    pero ahora lo que sucede es que necesito que al cerrar sesion redirija hacia el home ya que al redirijirnos al logout la pagina queda asi
    *

* **Respuesta / Solución aplicada**
    El prompt ayudo a solucionar el problema de la redireccion de la pagina al cerrar sesion ya sea admin o calquier usuario de esta forma redirigiendolo de vuelta al home pidiendo iniciar sesion o registrarse al querer empezar una compra.
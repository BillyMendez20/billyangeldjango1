from django.contrib import admin
from .models import Categoria, Producto

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'categoria', 'precio', 'cantidad', 'cantidad_vendida', 'cantidad_disponible')

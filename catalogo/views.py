from django.shortcuts import render
from .models import Categoria, Producto

def productos_por_categoria(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all().order_by('categoria')
    print(categorias, productos)
    return render(request, 'catalogo/productos_por_categoria.html', {'categorias': categorias, 'productos': productos})


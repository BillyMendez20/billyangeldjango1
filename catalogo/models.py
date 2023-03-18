from django.db import models

class Categoria(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField()
    cantidad_vendida = models.IntegerField(default=0)
    cantidad_disponible = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


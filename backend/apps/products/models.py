from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()  # Precio en centavos para evitar problemas de redondeo
    stock = models.IntegerField(default=0)
    attributes = models.JSONField(default=dict, blank=True)  # Para atributos personalizados como talla, color, etc.

    def __str__(self):
        return f"{self.name} (SKU: {self.sku})"
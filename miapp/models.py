from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    numero_de_telefono = models.IntegerField()
    producto = models.CharField(max_length=100)
    metodo_de_pago = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido} compró un/a {self.producto.lower()} con {self.metodo_de_pago.lower()}'

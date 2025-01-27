from django.db import models

class Comprar(models.Model):
    modelo = models.CharField(max_length=150)
    talle = models.CharField(max_length=2)
    mail = models.EmailField(max_length=254)
    direccion = models.CharField(max_length=300)
    banco = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.mail} - {self.modelo} - {self.talle}' 


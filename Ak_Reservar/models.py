from django.db import models

class Reservar(models.Model):
    modelo = models.CharField(max_length=150)
    talle = models.CharField(max_length=2)
    mail = models.EmailField(max_length=254)
    fecha = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.fecha} - {self.modelo} - {self.talle}'


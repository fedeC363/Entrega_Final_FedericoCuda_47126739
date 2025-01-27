from django.db import models

class Comentario(models.Model):
    autor = models.CharField(max_length=80)
    asunto = models.CharField(max_length=150)
    contenido = models.TextField(max_length=200)
    nombre_asistente = models.CharField(max_length=80)
    
    def __str__(self):
        return f'{self.asunto}'
    
class Comprar(models.Model):
    modelo = models.CharField(max_length=150)
    talle = models.CharField(max_length=2)
    mail = models.EmailField(max_length=254)
    direccion = models.CharField(max_length=300)
    banco = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.mail} - {self.modelo} - {self.talle}' 

class Reservar(models.Model):
    modelo = models.CharField(max_length=150)
    talle = models.CharField(max_length=2)
    mail = models.EmailField(max_length=254)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    
    

from django.db import models

class Comentario(models.Model):
    autor = models.CharField(max_length=80)
    asunto = models.CharField(max_length=150)
    contenido = models.TextField(max_length=200)
    nombre_asistente = models.CharField(max_length=80)
    
    def __str__(self):
        return f'{self.asunto}'
    
    
    

from django.db import models
class Curso(models.Model):
    nombre = models.CharField(max_length = 69)
    camada = models.IntegerField()
    
# Create your models here.

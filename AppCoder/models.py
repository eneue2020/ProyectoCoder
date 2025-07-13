from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email} - {self.profesion}"
    
class Entregable(models.Model):
    
    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} - {self.fecha_de_entrega} - {'Entregado' if self.entregado else 'No Entregado'}"
    

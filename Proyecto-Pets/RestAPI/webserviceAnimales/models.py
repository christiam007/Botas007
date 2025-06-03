from tkinter.constants import CASCADE

from django.db import models
from django.template.context_processors import request
from unicodedata import decimal


# Create your models here.

class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class ComidaAnimal(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)

    def __str__(self):
        return ("nombre: " + str(self.nombre) + "marca: " + str(self.marca) + "cantidad: "  +str(self.cantidad) +
                "precio: " + str(self.precio) + "animal: " + str(self.animal))


from django.db import models

# Create your models here.
from django.db import models

"""
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class Jugador(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Torneo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "Soy el torneo" + self.nombre

class JugadorTorneo(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)


    def __str__(self):
        return "Jugador -- " + str(self.jugador) + " Torneo -- " + str(self.torneo)

"""


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre

class Bota(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    talla = models.IntegerField(max_length=20)

    def __str__(self):
        return "marca: " + str(self.marca) + " modelo: " + str(self.modelo) + "talla: " + str(self.talla)





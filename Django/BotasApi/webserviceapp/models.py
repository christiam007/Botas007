from idlelib.pyparse import trans
from operator import truediv
from tkinter.constants import CASCADE

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
    username = models.CharField(primary_key=True, max_length=50, default='user_temp')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return "username: " + str(self.username) + "name: " + str(self.name) + "surname: " + str(self.surname) + "password: " + str(self.password)

class Bota(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    talla = models.CharField(max_length=2)
    autor = models.ForeignKey('Usuario',on_delete=models.CASCADE)

    def __str__(self):
        return "marca: " + str(self.marca) + " modelo: " + str(self.modelo) + " talla: " + str(self.talla)


class Cinturon(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return "marca: " + str(self.marca) + "modelo: " + str(self.modelo)




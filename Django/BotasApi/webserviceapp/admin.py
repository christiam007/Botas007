from django.contrib import admin
from .models import Torneo, Jugador,JugadorTorneo

admin.site.register(Torneo)
admin.site.register(Jugador)
admin.site.register(JugadorTorneo)

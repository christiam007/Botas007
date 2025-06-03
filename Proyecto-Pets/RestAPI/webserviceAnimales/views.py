import json
from itertools import product
from pydoc import resolve

from django.db.models import Q
from django.http import JsonResponse
from django.db import models
from django.shortcuts import render
from django.template.defaultfilters import escapeseq
from django.views.decorators.csrf import csrf_exempt
from datetime import time

from webserviceAnimales.models import ComidaAnimal, Animal


# Create your views here.
@csrf_exempt
def comidaAnimales(request):
    if request.method != 'GET':
        return JsonResponse({'Error':'No se puede usar otro metodo que no sea Get'})

    especie = request.GET.get("especie")

    if especie is None:
        comidaAnimales = ComidaAnimal.objects.all()
    else:

        animal = Animal.objects.get(especie__icontains=especie)

        comidaAnimales = ComidaAnimal.objects.filter(animal=animal)

        #animales = Animal.objects.filter(especie__icontains=especie)

       # comidaAnimales = ComidaAnimal.objects.filter(animal__in=animales)
#
        #


    data = []
    for comidaAnimal in comidaAnimales:
        data.append({
            'id': comidaAnimal.id,
            'nombre': comidaAnimal.nombre,
            'marca': comidaAnimal.marca,
            'animal': comidaAnimal.animal.nombre,
            'especie': comidaAnimal.animal.especie
        })
    return JsonResponse({'comidaAnimal': data})



@csrf_exempt
def datos_vecinos(request):
    if request.method != 'POST':
        return JsonResponse({'Error':'Metodo no soportado, ingrese un POST '}, status=405)

    json_data = json.loads(request.body)

    print(json_data)

    nombre = json_data.get('name')
    apellido = json_data.get('suername')
    trabajo = json_data.get('job')
    edad = json_data.get('edad')

    print(f"nombre del nuevo vecino:{nombre} Apellido:: {apellido} Trabaja de: {trabajo} Dentro de 10 años tendra {10 +edad}")

    return JsonResponse({})


@csrf_exempt
def presidentes(request):
    if request.method != 'POST':
        return JsonResponse({'Error':'Metodo no soportado, ingrese un POST '}, status=405)

    json_data = json.loads(request.body)

    print(json_data)

    nombre = json_data.get('nombre')
    apellidos = json_data.get('apellidos')
    agenda_politica = json_data.get('agendaPolitica', {})
    objetivo = agenda_politica.get('objetivo')
    fecha_nacimiento = json_data.get('fechaNacimiento')


    print(f"Nombre del presidente: {nombre} Apellidos: {apellidos} Objetivo político: {objetivo} Fecha de nacimiento: {fecha_nacimiento}")

    return JsonResponse({})


@csrf_exempt
def superheroes(request):
    if request.method != 'POST':
        return JsonResponse({'Error':'Metodo no soportado, ingrese un POST '}, status=405)

    json_data = json.loads(request.body)

    print(json_data)

    nombre = json_data.get('nombre')
    color_favorito = json_data.get('color_favorito')
    dispositivo = json_data.get('dispositivo')
    formas = json_data.get('formas', [])

    print(f"Nombre del superhéroe:{nombre}")
    print(f"Color_favorito: {color_favorito}")
    print(f"Dispositivo: {dispositivo}")
    print(f"Formas:{formas}")

    for forma in formas:
        print(forma.get("nombre"))

    return JsonResponse({})






























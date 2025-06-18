import json
import secrets
from venv import create
from wsgiref.util import request_uri

import bcrypt
from django.db.models import Q
from django.db.models.fields import return_None
from django.template.defaultfilters import safeseq
from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from unicodedata import category
from urllib3 import request

from webserviceapp.models import Bota, Usuario, Cinturon


# Create your views here.
def my_first_endpoint_empty(request):
    return JsonResponse({})

def my_name(request):
    return JsonResponse({"nombre":"christian"})

def suerte_nota(request):
    json_diccionario={
        "Suerte":"Mucha",
        "nota": 10
    }
    return JsonResponse(json_diccionario)

def array_json(request):
    return JsonResponse([1, 2, 3], safe=False)


def arrayLetras_json(request):
    return JsonResponse( ["a","b","c"], safe=False)


def arraynombres_json(request):
    return JsonResponse([{"nombre":"Iago"}, {"Nombre":"Christian"}], safe=False)

def detalle_articulo(request,articulo_id):

    return JsonResponse({})

def mostrar_productos(request, categoria, id):

    return JsonResponse({"very": "good"})

def mostrar_productos_recibidos(request,articulo):
    return JsonResponse({"articulo":articulo})

def solo_recibir_enteros(request, numero):

    return JsonResponse({"Ok": "Mackey"})


def listarProductos(request):
    categoria = request.GET.get('categoria')

    resultado = {"marca":'modelo'}

    print(categoria)
    return JsonResponse(resultado)


def ver_producto(request, id):
    color = request.GET.get('color')

    print(id)
    print(color)

    return JsonResponse({"ok": 'Mackey'})

def buscar_productos(request):
    categoria = request.GET.get('categoria')
    precio = request.GET.get('precio')

    if categoria is None and precio is None:
        print("No mandaste nada!!!")

        return JsonResponse({"mensaje": "No mandaste nada!!!"})

    elif categoria is None and precio is not None:
        print("Solo mandaste precio: El siguiente " + str(precio))

        return JsonResponse({"mensaje": "Sólo mandaste precio: El siguiente " + precio })

    elif categoria is not None and precio is None:
        print("Solo mandaste categoría: Es la siguiente" + str(categoria))
        return JsonResponse({ "mensaje": "Sólo mandaste categoría: Es la siguiente " + categoria })

    else:
        print("Mandaste ambos por categoria: " + str(categoria) + "y precio: " + str(precio))

    return JsonResponse({ "mensaje": "Mandaste ambos" })


def search_the_bots(request, id):
    if request.method != 'GET':
        return JsonResponse({
            'mensaje': 'Método no permitido'
        }, status=405)

    try:
        bota = Bota.objects.get(id=id)
    except Bota.DoesNotExist:
        return JsonResponse({
            'mensaje': 'Bota no encontrada'
        }, status=404)


    return JsonResponse({
        'marca': bota.marca,
        'modelo': bota.modelo,
        'talla': bota.talla
    }, status=200)

def listar_botas(request):
    #Metodo 1 (funcional)
    botas = Bota.objects.all()
    data=[]
    for bota in botas:
        data.append({
            "id": bota.id,
            "marca":bota.marca,
            "modelo":bota.modelo,
            "talla": bota.talla
        })
    return JsonResponse(data, safe=False, status=200)

    """
    Metodo 2 (Pythonic)

    data = [{"id": bota.id} for bota in botas]

    # Metodo 3 (funcional)
    data = list(map(lambda x: {"id": x.id}, botas))
    """


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    data=[{"id":usuario.id,"nombre":usuario.nombre} for usuario in usuarios]

    return JsonResponse(data, safe=False, status=200)


@csrf_exempt
def botas(request):
    if request.method != 'GET':
        return JsonResponse({'Error': 'Metodo no permitido. Solo se acepta get.'}, status=405)

    s = request.GET.get("search")
    if s is None:
        botas = Bota.objects.all()
    else:
        botas = Bota.objects.filter (Q(modelo__icontains=s) | Q(marca__icontains=s) | Q(talla__icontains=s))

    data = []
    for bota in botas:
        data.append({
            'id': bota.id,
            'marca': bota.marca,
            'modelo': bota.modelo,
            'talla': bota.talla
        })

    return JsonResponse({'botas': data})

@csrf_exempt
def usuario(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print(request.body)
        return JsonResponse({'ok':'makey'})



@csrf_exempt
def registro(request):
    if request.method != 'POST':
        return JsonResponse({'Error': 'Metodo no soportado, ingrese un POST'}, status=405)

    json_registro = json.loads(request.body)
    print(json_registro)

    username = json_registro.get('username')
    name   = json_registro.get('name')
    surname  = json_registro.get('surname')
    password = json_registro.get('password')

    Usuario.objects.create(username=username, name=name, surname=surname, password=password)

    return JsonResponse({'mensaje':'usuario creado'}, status=201)


@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({'Error': 'Metodo no soportado, ingrese Post'}, status=405)

    json_data = json.loads(request.body)
    print(json_data)

    username = json_data.get('username')
    password = json_data.get('password')

    try:
        usuario = Usuario.objects.get(username = username)

        password_hasheada = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')

        token = secrets.token_hex(32)


        if bcrypt.checkpw(password.encode('utf8'), usuario.password.encode('utf8')):
            usuario.token = token
            usuario.save()

            return JsonResponse({'token':token}, status=200)

        return JsonResponse({'Error':'Contraseña incorrecta'}, status=401)

    except Usuario.DoesNotExist:
         return JsonResponse({'Error': 'Usuario no existe'}, status=404)


@csrf_exempt
def subir_bota(request):

    t = request.headers.get('token')


    if not t:
        return JsonResponse({'mensaje':'No existe token!!'},status=401)

    try:
        usuario = Usuario.objects.get(token=t)
    except Usuario.DoesNotExist:
        return JsonResponse({'mensaje': 'token no es valido'}, status=401)

    bota_json = json.loads(request.body)

    marca = bota_json.get("marca")
    modelo = bota_json.get("modelo")
    talla = bota_json.get("talla")


    Bota.objects.create(marca=marca, modelo=modelo, talla=talla,autor=usuario)

    return JsonResponse({'Mensaje':'Bota cargada con existo'}, status=201)


def listar_cinturon(request):
    if request.method != 'GET':
        return JsonResponse({'Error':'Metodo no soportado, use Get'}, status=405)


    cinturones = Cinturon.objects.all()

    data = []

    for cinturon in cinturones:
        data.append({
            'id':cinturon.id,
            'marca':cinturon.marca,
            'modelo':cinturon.modelo

        })
    return JsonResponse(data,safe=False,status=200)





































































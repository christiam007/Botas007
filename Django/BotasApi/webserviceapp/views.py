from django.template.defaultfilters import safeseq
from django.urls import path
from django.http import JsonResponse
from unicodedata import category


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

    elif categoria is None and precio is not None:
        print("Solo mandaste precio: El siguiente " + str(precio))

    elif categoria is not None and precio is None:
        print("o mandaste categoría: Es la siguiente" + str(categoria))

    else:
        print("Mandaste ambos por categoría: " + str(categoria) + "y precio:" + str(precio))

    return JsonResponse({"ok": "Mackey"})











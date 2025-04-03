from django.template.defaultfilters import safeseq
from django.urls import path
from django.http import JsonResponse

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






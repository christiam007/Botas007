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






from django.urls import path
from django.http import JsonResponse

# Create your views here.
def my_first_endpoint_empty(request):
    return JsonResponse({})

def my_name(request):
    return JsonResponse({"nombre":"christian"})






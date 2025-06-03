from django.contrib import admin

from webserviceAnimales.models import ComidaAnimal, Animal

# Register your models here.

admin.site.register(Animal)
admin.site.register(ComidaAnimal)

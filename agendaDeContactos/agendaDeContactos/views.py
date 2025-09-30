from django.http import HttpResponse 
from django.shortcuts import render
from .models import Contacto


def inicio(request): 
    nombre = "Marcelo Hermosilla"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!") 

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'agenda/lista.html', {'contactos': contactos}) 
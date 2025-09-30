from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .form import ContactoForm

# Create your views here.

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'personas/lista_contactos.html', {'contactos': contactos})

def detalle_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'personas/detalle_contacto.html', {'contacto': contacto})

def nuevo_contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'personas/nuevo_contacto.html', {'form': form})

def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form    .save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'personas/editar_contactos.html', {'form': form})

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'personas/eliminar_contactos.html', {'contacto': contacto})


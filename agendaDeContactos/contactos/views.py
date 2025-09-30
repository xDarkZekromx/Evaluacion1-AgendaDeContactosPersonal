from django.shortcuts import render, get_list_or_404, redirect
from .models import Contacto
from .form import ContactoForm

# Create your views here.

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'personas/lista_contactos.html', {'contactos': contactos})

def detalle_contacto(request, pk):
    contacto = get_list_or_404(Contacto, pk=pk)
    return render(request, 'personas/detalle_contacto.html', {'contacto': contacto})

def nuevo_contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalle_contacto')
    else:
        form = ContactoForm()
    return render(request, 'personas/form_contactos.html', {'form': form})

def editar_contacto(request, pk):
    contacto = get_list_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('detalle_contacto')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'personas/form_contactos.html', {'form': form})

def eliminar_contacto(request, pk):
    contacto = get_list_or_404(Contacto, pk=pk)
    if request.method == "POST":
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'personas/contacto_confirm_delete.html', {'contacto': contacto})


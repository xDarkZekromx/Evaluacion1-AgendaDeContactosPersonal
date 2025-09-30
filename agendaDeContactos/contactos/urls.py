from django.urls import path
from . import views

urlpatterns = [
    path('personas/', views.lista_contactos, name='lista_contactos'),
    path('personas/nuevo/', views.nuevo_contacto, name='nuevo_contacto'),
    path('personas/<int:pk>/', views.detalle_contacto, name='detalle_contacto'),
    path('personas/<int:pk>/editar/', views.editar_contacto, name='editar_contacto'),
    path('personas/<int:pk>/eliminar/', views.eliminar_contacto, name='eliminar_contacto'),
    
]
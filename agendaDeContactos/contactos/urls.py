from django.urls import path
from . import views

urlpatterns = [
    path('contactos/', views.lista_contactos, name='lista_contactos'),
    path('contactos/nuevo/', views.nuevo_contacto, name='nuevo_contacto'),
    path('contactos/<int:pk>/', views.detalle_contacto, name='detalle_contacto'),
    path('contactos/<int:pk>/editar/', views.editar_contacto, name='editar_contacto'),
    path('contactos/<int:pk>/eliminar/', views.eliminar_contacto, name='eliminar_contacto'),
]
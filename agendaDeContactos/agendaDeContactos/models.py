from django.db import models 
from django.core.validators import RegexValidator


class Contacto(models.Model): 
    nombre = models.CharField(max_length=100) 
    telefono = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^[29]\d{8}$',
                message="El número debe comenzar con 2 (casa) o 9 (móvil) y tener 9 dígitos."
            )
        ]
    )
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)

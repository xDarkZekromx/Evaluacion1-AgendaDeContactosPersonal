from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Contacto(models.Model): 
    nombre = models.CharField(max_length=100) 
    telefono = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^[29]\d{8}$',
                message="El número debe comenzar con 2 (casa) o 9 (móvil) y tener 9 digitos."
            )
        ]
    )
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
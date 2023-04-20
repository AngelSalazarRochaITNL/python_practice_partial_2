from django.db import models
from empleado.models import Empleado

# Create your models here.
class Evaluacion(models.Model):
    fecha_evaluacion = models.DateField()
    desempenio = models.IntegerField()
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null = True)
    def __str__(self) -> str:
        return f'Evaluacion {self.id}: {self.desempenio}'

class Punto(models.Model):
    numero = models.IntegerField
    pregunta = models.CharField(max_length=1)
    def __str__(self) -> str:
        return f'Punto {self.id} : {self.numero} : {self.pregunta}'

class Respuesta(models.Model):
    puntuacion = models.IntegerField()
    numero_punto = models.ForeignKey(Punto, on_delete=models.SET_NULL, null = True)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.SET_NULL, null = True)

    def __str__(self) -> str:
        return f'Respuesta {self.id} : {self.numero_punto} : {self.evaluacion}'



from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Empleado {self.id} : {self.nombre}'
    

class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Archivo {self.id} : {self.nombre}'
    
class Archivo_Empleado(models.Model):
    nomrbe_real = models.CharField(max_length=255)
    ruta = models.CharField(max_length=255)
    archivo = models.ForeignKey(Archivo, on_delete=models.SET_NULL, null = True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null = True)
    def __str__(self) -> str:
        return f'Archivo {self.archivo}: Empleado {self.empleado}'
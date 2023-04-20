from django.db import models

# Create your models here.

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_lenght=255)
    pe = models.CharField(max_lenght=255)
    defensa = models.CharField(max_lenght=255)
    ataque = models.CharField(max_lenght=255)
    

class Ruta(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.SET_NULL, null  = True)
    tipo = models.CharField(max_lenght=255)
    hostilidad = models.CharField(max_lenght=255)

class Npc(models.Model):
    nombre = models.CharField(max_lenght=255)
    pv = models.CharField(max_lenght=255)
    ataque = models.CharField(max_lenght=255)

class Dialogos(models.Model):
    npc = models.ForeignKey(Personaje, on_delete=models.SET_NULL, null  = True)
    texto = models.CharField(max_lenght=255)


class Camino(models.Model):
    spawns = models.CharField(max_lenght=255)

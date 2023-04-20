from django.contrib import admin
from gestorapp.models import Personaje, Npc, Ruta, Dialogos, Camino

# Register your models here.
admin.site.register(Personaje)
admin.site.register(Ruta)
admin.site.register(Npc)
admin.site.register(Dialogos)
admin.site.register(Camino)
from django.contrib import admin
from evaluacion.models import Evaluacion, Respuesta, Punto

# Register your models here.
admin.site.register(Evaluacion)
admin.site.register(Punto)
admin.site.register(Respuesta)
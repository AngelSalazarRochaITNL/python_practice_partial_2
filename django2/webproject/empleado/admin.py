from django.contrib import admin
from empleado.models import Empleado, Archivo, Archivo_Empleado

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Archivo)
admin.site.register(Archivo_Empleado)
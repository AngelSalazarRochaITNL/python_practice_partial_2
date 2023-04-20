from django.shortcuts import render

# Create your views here.
from empleado.models import Empleado, Archivo, Archivo_Empleado


# Create your views here.
def indexEmpleados(request):
    formaEmpleados = Empleado.objects.all()
    formaArchivo = Archivo.objects.all()
    formaArchivo_Empleado = Archivo_Empleado.objects.all()

    return render(
        request,
        'indexEmpleados.html',
        {
            'formaEmpleados': formaEmpleados, 
            'formaArchivo': formaArchivo,
            'formaArchivo_empleado': formaArchivo_Empleado
        })


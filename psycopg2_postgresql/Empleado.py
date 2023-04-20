from logger_base import log

class Empleado:
    def __init__(self, id_empleado = None, nombre = None, puesto = None) -> None:
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._puesto = puesto

    def __str__(self) -> str:
        return f"""
        Id empleado: {self._id_empleado}, Nombre: {self._nombre}, Puesto: {self._puesto}
        """
    
    @property
    def id_empleado(self):
        return self._id_empleado
    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def Puesto(self):
        return self._puesto
    @Puesto.setter
    def Puesto(self, puesto):
        self._puesto = puesto
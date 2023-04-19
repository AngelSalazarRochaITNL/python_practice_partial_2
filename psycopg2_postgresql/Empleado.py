from logger_base import log

class Empleado:
    def __init__(self, id_empleado = None, nombre = None, apellido = None, puesto = None, supervisor = None, fecha_contratacion = None) -> None:
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._apellido = apellido
        self._puesto = puesto
        self._supervisor = supervisor
        self._fecha_contratacion = fecha_contratacion

    def __str__(self) -> str:
        return f"""
        Id empleado: {self._id_empleado}, Nombre: {self._nombre}
        Apellido: {self._apellido}, Puesto: {self._puesto}
        """
    
    @property
    def idEmpleado(self):
        return self._id_empleado
    @idEmpleado.setter
    def idEmpleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def idEmpleado(self):
        return self._id_empleado
    @idEmpleado.setter
    def idEmpleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def idEmpleado(self):
        return self._id_empleado
    @idEmpleado.setter
    def idEmpleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def idEmpleado(self):
        return self._id_empleado
    @idEmpleado.setter
    def idEmpleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def idEmpleado(self):
        return self._id_empleado
    @idEmpleado.setter
    def idEmpleado(self, id_empleado):
        self._id_empleado = id_empleado
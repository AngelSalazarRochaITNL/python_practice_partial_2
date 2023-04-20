from logger_base import log

class Archivo_Empleado:
    def __init__(self, id_archivo = None, id_empleado = None, nombre_real = None, ruta = None) -> None:
        self._id_archivo = id_archivo
        self._id_empleado = id_empleado
        self._nombre_real = nombre_real
        self._ruta = ruta

    def __str__(self) -> str:
        return f"""
        Tipo Archivo : {self._id_archivo}, Empleado : {self._id_empleado}, Archivo: {self._nombre_real}, Ruta : {self._ruta}
        """
    
    @property
    def id_archivo(self):
        return self._id_archivo
    @id_archivo.setter
    def id_archivo(self, id_archivo):
        self._id_archivo = id_archivo

    @property
    def id_empleado(self):
        return self._id_empleado
    @id_empleado.setter
    def id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    @property
    def Nombre_Real(self):
        return self._nombre_real
    @Nombre_Real.setter
    def Nombre_Real(self, nombre_real):
        self._nombre_real = nombre_real

    @property
    def Ruta(self):
        return self._ruta
    @Ruta.setter
    def Ruta(self, ruta):
        self._ruta = ruta
from logger_base import log

class Archivo:
    def __init__(self, id_archivo = None, nombre_archivo = None) -> None:
        self._id_archivo = id_archivo
        self._nombre_archivo = nombre_archivo

    def __str__(self) -> str:
        return f"""
        Archivo : {self._id_archivo}, Nombre: {self._nombre_archivo}
        """
    
    @property
    def id_archivo(self):
        return self._id_archivo
    @id_archivo.setter
    def id_archivo(self, id_archivo):
        self._id_archivo = id_archivo

    @property
    def Nombre_Archivo(self):
        return self._nombre_archivo
    @Nombre_Archivo.setter
    def Nombre_Archivo(self, nombre_archivo):
        self._nombre_archivo = nombre_archivo

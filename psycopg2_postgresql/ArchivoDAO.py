from Archivo import Archivo
from cursorDelPool import CursorDelPool
from logger_base import log

class ArchivoDAO: #Data access object

    _SELECCIONAR= "SELECT * FROM archivo ORDER BY id_archivo"
    _INSERTAR = "INSERT INTO archivo(id_archivo, nombre_archivo) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE archivo SET nombre = %s, puesto = %s WHERE id_archivo = %s"
    _ELIMINAR = "DELETE FROM archivo WHERE id_archivo = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            archivos = []
            for r in registros:
                archivo = Archivo(r[0],r[1])
                archivos.append(archivo)
            return archivos
    
    @classmethod
    def insertar(cls,archivo):
        with CursorDelPool() as cursor:
            valores = (archivo.id_archivo, archivo.Nombre_Archivo)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,archivo):
        with CursorDelPool() as cursor:
            valores = (archivo.Nombre, archivo.Puesto, archivo.id_archivo)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,archivo):
        with CursorDelPool as cursor:
            valores = (archivo.id_archivo,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #Insertar
    archivo1 = Archivo(id_archivo="5", nombre_archivo="CONSTANCIA DE ESTUDIOS")
    archivosInsertados = ArchivoDAO.insertar(archivo1)
    archivo2 = Archivo(id_archivo="6",nombre_archivo="ANTIDOPING")
    archivosInsertados = ArchivoDAO.insertar(archivo2)
    log.debug(f"Archivos Agregados: {archivosInsertados}")
    #Leer
    archivos = ArchivoDAO.seleccionar()
    for a in archivos:
        log.debug(a)

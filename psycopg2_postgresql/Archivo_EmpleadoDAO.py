from Archivo_Empleado import Archivo_Empleado
from cursorDelPool import CursorDelPool
from logger_base import log

class Archivo_EmpleadoDAO:

    _SELECT = "SELECT * FROM archivo_empleado ORDER BY id_archivo_e, id_empleado_a"
    _INSERT = """INSERT INTO archivo_empleado(id_archivo_e, id_empleado_a, nombre_real, ruta) 
                VALUES (%s, %s, %s, %s)"""
    _UPDATE = "UPDATE archivo_empleado SET nombre_real = %s, ruta = %s WHERE id_archivo_e = %s and id_empleado_a = %s"
    _DELETE = "DELETE FROM archivo_empleado WHERE id_archivo_e = %s and id_empleado_a = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            archivos_empleados = []
            for r in registros:
                archivo_empleado = Archivo_Empleado(r[0],r[1],r[2],r[3])
                archivos_empleados.append(archivo_empleado)
            return archivos_empleados
    
    @classmethod
    def insertar(cls,archivo_empleado):
        with CursorDelPool() as cursor:
            valores = (archivo_empleado.id_archivo, archivo_empleado.id_empleado, archivo_empleado.Nombre_Real , archivo_empleado.Ruta)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,archivo_empleado):
        with CursorDelPool() as cursor:
            valores = (archivo_empleado.Nombre_Real, archivo_empleado.Ruta, archivo_empleado.id_archivo, archivo_empleado.id_empleado)
            cursor.execute(cls._UPDATE, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,archivo_empleado):
        with CursorDelPool as cursor:
            valores = (archivo_empleado.id_archivo, archivo_empleado.id_empleado)
            cursor.execute(cls._DELETE, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #Insertar
    archivo_empleado1 = Archivo_Empleado(id_archivo="1", id_empleado="1", nombre_real="acta_rocha.pdf", ruta="expedientes/rocha")
    archivoEmpleadoInsertado = Archivo_EmpleadoDAO.insertar(archivo_empleado1)
    archivo_empleado1 = Archivo_Empleado(id_archivo="2", id_empleado="1", nombre_real="rfc_rocha.pdf", ruta="expedientes/rocha")
    archivoEmpleadoInsertado = Archivo_EmpleadoDAO.insertar(archivo_empleado1)
    log.debug(f"Archivos subidos: {archivoEmpleadoInsertado}")

    #Leer
    archivos_empleados = Archivo_EmpleadoDAO.seleccionar()
    for ae in archivos_empleados:
        log.debug(ae)
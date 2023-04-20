from Empleado import Empleado
from cursorDelPool import CursorDelPool
from logger_base import log

class EmpleadoDAO: #Data access object

    _SELECCIONAR= "SELECT * FROM empleado ORDER BY id_empleado"
    _INSERTAR = "INSERT INTO empleado(id_empleado, nombre,puesto) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE empleado SET nombre = %s, puesto = %s WHERE id_empleado = %s"
    _ELIMINAR = "DELETE FROM empleado WHERE id_empleado = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            empleados = []
            for r in registros:
                empleado = Empleado(r[0],r[1],r[2])
                empleados.append(empleado)
            return empleados
    
    @classmethod
    def insertar(cls,empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.id_empleado, empleado.Nombre, empleado.Puesto)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,empleado):
        with CursorDelPool() as cursor:
            valores = (empleado.Nombre, empleado.Puesto, empleado.id_empleado)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,empleado):
        with CursorDelPool as cursor:
            valores = (empleado.id_empleado,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #Insertar
    empleado1 = Empleado(id_empleado="7", nombre="Angel",puesto= "Administrador")
    empleadosInsertadas = EmpleadoDAO.insertar(empleado1)
    empleado2 = Empleado(id_empleado="8",nombre="Ricardo",puesto= "Contador")
    empleadosInsertadas = EmpleadoDAO.insertar(empleado2)
    log.debug(f"Empleados Agregadas: {empleadosInsertadas}")
    #Leer
    empleados = EmpleadoDAO.seleccionar()
    for e in empleados:
        log.debug(e)

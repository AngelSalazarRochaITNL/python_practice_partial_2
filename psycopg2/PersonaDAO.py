from psycopg2.Persona import Persona
from psycopg2.cursorDelPool import CursorDelPool
from psycopg2.logger_base import log

class PersonaDAO:

    _SELECCIONAR= "SELECT * FROM persona ORDER BY id"
    _INSERTAR = "INSERT INTO persona(nombre,edad,correo) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s, edad =%s, correo =%s WHERE id = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Edad ,persona.Correo)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre,persona.Edad, persona.Correo,  persona.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,persona):
        with CursorDelPool as cursor:
            valores = (persona.id,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
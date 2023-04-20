from psycopg2.logger_base import log

class Persona:
    def __init__(self, idpersona = None, nombre=None, edad=None, correo=None) -> None:
        self._idpersona = idpersona
        self._nombre = nombre
        self._edad = edad
        self._correo = edad
    
    def __str__(self) -> str:
        
        return f"""
        Id Persona: {self._idpersona}, Nombre: {self._nombre}
        Edad: {str(self._edad)}, Correo: {self._correo}
        """
    
    @property
    def idPersona(self):
        return self._idpersona
    @idPersona.setter
    def idPersona(self, idpersona):
        self._idpersona = idpersona

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def Edad(self):
        return self._edad
    @Edad.setter
    def Edad(self, edad):
        self._edad = edad
    
    @property
    def Correo(self):
        return self._correo
    @Correo.setter
    def Correo(self, correo):
        self._correo = correo

if __name__ == "__main__":
    persona1 = Persona(1,"Juan",20,"Jperez@gmail.com")
    log.debug(persona1)
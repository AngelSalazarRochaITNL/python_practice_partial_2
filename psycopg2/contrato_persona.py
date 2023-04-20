from psycopg2.logger_base import log

class contrato_persona:
    def __init__(self, idpersona = None, idcontrato=None) -> None:
        self._idpersona = idpersona
        self._idcontrato = idcontrato
    
    def __str__(self) -> str:
        
        return f"""
        Id Persona: {self._idpersona}, Id Contrato: {self._idcontrato}
        """
    
    @property
    def idPersona(self):
        return self._idpersona
    @idPersona.setter
    def idPersona(self, idpersona):
        self._idpersona = idpersona

    @property
    def idContrato(self):
        return self._idcontrato
    @idContrato.setter
    def idContrato(self, idcontrato):
        self._idcontrato = idcontrato

if __name__ == "__main__":
    contrato_persona1 = contrato_persona(1,1)
    log.debug(contrato_persona1)
from psycopg2.logger_base import log

class Contrato:
    def __init__(self, idContrato = None, noContrato=None, costo=None, feInicio=None, feFinal=None) -> None:
        self._idContrato = idContrato
        self._noContrato = noContrato
        self._costo = costo
        self._feInicio = feInicio
        self._feFinal = feFinal
    
    def __str__(self) -> str:
        
        return f"""
        Id Contrato: {self._idContrato}, Numero contrato: {str(self._noContrato)}, Costo: {str(self._costo)},
        Fecha Inicio: {self._feInicio}, Fecha Final: {self._feFinal}
        """

    @property
    def idContrato(self):
        return self._idContrato
    @idContrato.setter
    def idContrato(self, idcontrato):
        self._idContrato = idcontrato

    @property
    def noContrato(self):
        return self._noContrato
    @noContrato.setter
    def noContrato(self, nocontrato):
        self._noContrato = nocontrato

    @property
    def Costo(self):
        return self._costo
    @Costo.setter
    def Costo(self, costo):
        self._costo = costo

    @property
    def feInicio(self):
        return self._feInicio
    @feInicio.setter
    def feInicio(self, feinicio):
        self._feInicio = feinicio
    
    @property
    def feFinal(self):
        return self._feFinal
    @feFinal.setter
    def feFinal(self, fefinal):
        self._feFinal = fefinal

if __name__ == "__main__":
    contrato1 = Contrato(1,10,20,00-00-00,00-00-00)
    log.debug(contrato1)
import logging as log

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s: %(levelname)s [$(filename)s] :%(lineno)s %(message)s",
                datefmt = '%I:%M:%S %p',
                handlers=[log.FileHandler('capa_datos.log'),
                          log.StreamHandler()
                ])

if __name__ == "_main_":
    log.debug("Message debug")
    log.warning("Message warning")
    log.error("Monsaje error")
    log.critical("Message critico")
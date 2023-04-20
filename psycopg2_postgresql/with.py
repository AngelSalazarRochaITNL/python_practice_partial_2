import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="Postgres",
                            password="Yon1thek1",
                            host="127.0.0.1",
                            port="5432",
                            database="postgres")

log.debug(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT TO persona(nombre, apellido, email) Values(%s)"
            valores = (
                ("Juan", "Perez", "Juan@gmail.com"),
                ("Maria", "Teresa", "Maria@gmail.com")
            )
            cursor.executemany(sentencia,valores)
            registrosInsert = cursor.rowcount
            log.debug(f"Regisros insertados: {registrosInsert}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()

try:
    with conexion:
        with conexion.cursor as cursor:
             sentencia = "UPDATE persona SET nombre =%s, apellido=%s , email=%s, Values%s"
             values=(
                    ("Pedro","Pascal","pascal@gmail.com",1)
                    ("Josel","Sanchez","sanchez@gmail.com",2)
                    )
             cursor.executemany(sentencia,values)
             registrosActualizados = cursor.rowcount
             log.debug(F'Registros actualizados: {registrosActualizados}')
     
except Exception as e:
     log.error(e)
finally:
     conexion.close()

try:
     with conexion:
          with conexion.cursor() as cursor:
             sentencia = "DELETE FROM persona WHERE idpersona = %s"
             entrada = input("IDs A ELIMINAR: ")
             valores=(tuple(entrada.split(",")),)
             cursor.execute(sentencia,valores)
             resgistrosEliminados = cursor.rowcount
             log.debug(f"Registros eliminados: {resgistrosEliminados}")
     
except Exception as e:
     log.error(e)
finally:
     conexion.close()

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = " DELETE FROM persona WHERE idpersona IN %s"
            entrada = input ("ID A ELIMINAR: ")
            valores = (tuple(entrada.split(",")),)
            cursor.execute(sentencia,valores)
            registrosEliminados = cursor.rowcount
            log.debug(f"Registros eliminados: {registrosEliminados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()
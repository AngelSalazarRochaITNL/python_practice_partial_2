import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres",
                            password="Yon1thek1",
                            host="127.0.0.1",
                            port=5432,
                            database="postgres")

try:
    conexion.autocommit=False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO empleado(idempleado, nombre, puesto) Values(%s,%s,%s)"
    idempleado = 2
    nombre="Rocha"
    puesto="DevOp"
    valores=(idempleado,nombre,puesto)
    cursor.execute(sentencia, valores)
    log.debug("insert")
    sentencia="UPDATE empleado SET nombre =%s WHERE id_empleado=%s"
    valores=("Angel Salazar",2)
    cursor.execute(sentencia,valores)
    log.debug("Sentencia update")
    conexion.commit()
except Exception as e:
    conexion.rollback()
    log.error(e)



cursor = conexion.cursor()
cursor.execute("SELECT nombre FROM empleado")
resultados = cursor.fetchall()
print(resultados)
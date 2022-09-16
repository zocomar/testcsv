# conectar a la base de datos mysql y hacer una consulta
import mysql.connector
from mysql.connector import errorcode
# datos de conexion
config = {  
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'test',
    'raise_on_warnings': True,
}
# conectar a la base de datos
try:
    cnx = mysql.connector.connect(**config)
    print("Conectado a la base de datos")
    # crear un cursor
    cursor = cnx.cursor()
    # ejecutar una consulta
    cursor.execute("SELECT * FROM preba")
    # obtener los resultados
    rows = cursor.fetchall()
    # mostrar los resultados
    for row in rows:
        print(row)
    # cerrar el cursor
    cursor.close()
    # cerrar la conexion
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuario o contraseña incorrectos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Base de datos no encontrada")
    else:
        print(err)
else:
    cnx.close()
    print("Desconectado de la base de datos")

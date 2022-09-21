# convertir csv en mysql    
import csv
import mysql.connector
from mysql.connector import errorcode
# datos de conexion
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'testcsv',
    'raise_on_warnings': True,
    }
# convertir csv en mysql
# abrir el archivo csv
# charset utf-8 para que no de problemas con los acentos 
with open('economia_export.txt', 'r', encoding='utf-8') as archivo_csv:
    # crear un lector csv
    lector_csv = csv.reader(archivo_csv, delimiter=';')
    # leer el archivo csv
    for fila in lector_csv:
        print(fila)  
    # insertar los datos en la tabla    
        try:    
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            sql = "insert into grados (anual,universidad,rama,medida,valor,vacio) values (%s, %s, %s, %s, %s,%s)"
            cursor.execute(sql, fila)
            cnx.commit()
            cursor.close()
            cnx.close() 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
                print("algo esta mal con el usuario o la contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:     
                print("la base de datos no existe")
            else:
                print(err)
        else:
            cnx.close()
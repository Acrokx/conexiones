#Instalar paquetes
#pip install mysql-connector-python

#Importamos el modulo para la conexion con MySQL
import mysql.connector

try:
    #Establece conexion con la base de datos XAMPP
    conn = mysql.connector.connect(  
        host="localhost",         #Direccion del servidor de la base de datos (en este caso, local)
        user="root",              #Usuario de MySQL
        password="",              #Contraseña del usuario de mySQL (debe configurarse si tiene una)
        database="Ficha3066478",  #Descomentar si se quiere conectar a una base de datos especifica
    ) 

    # Si la conexion se establece correctamente, impimir un mesaje de exito
    print(conn)
    print("\u2705 Conexion exitosa")
    print(f"\U0001F50E Tipo de objeto de conexión: {type(conn)}") # Muestra el tipo de objeto de conexion

    # Creamos un cursor para ejecutar comandos SQL
    cursor=conn.cursor()

    #Ejecutamos una consulta SQL para listar las bases de datos en el servidor
    cursor.execute("SHOW DATABASE")

    #Iteramos sobre los resultados y los imprimimos
    for db in cursor:
        print(db)

except mysql.connector.Error as err:
    # Capturamos cualquier error de conexion y lo imprime
    print(f"\u2705 Error al conectar con MySQL: {err}")

finally:
    # Cerramos la conexion si se establecio correctamente
    if "conn" in locals() and conn.is_connected():
        cursor.close() # Cerramos el cursor
        conn.close() # Cerramos la conexion
        print(" \u2757 Conexion cerrada")


# Importar modulo
# import mysql.connector
import sqlite3

"""
# ========== MySQL ==========
def Connect():
    database = mysql.connector.Connect(
        host="localhost",
        user="root",
        password="",
        port=3306
        #,database="agrofit"
    )
    # Cursor que nos permite ejecutar las consultas
    cursor = database.cursor(buffered=True)

    # print("✓ Conexión con MySQL establecida correctamente.")

    return [database, cursor]
"""


# ========== SQLite ==========
def Connect_SQLite():
    # Conexion a base de datos
    connect = sqlite3.connect("backend/data/agrofit.db")
    # Crear cursor
    cursor = connect.cursor()
    # Cerrar la conexiòn
    # connect.close()

    # Retornar los objetos requeridos
    return [connect, cursor]

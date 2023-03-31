import sqlite3 

class ConexionDB:
    def __init__(self):
        self.base_datos = "database/peliculas.db" 
        self.conexion = sqlite3.connect(self.base_datos)  # Conectar a la base de datos
        self.cursor = self.conexion.cursor()   # Obtener un cursor para ejecutar instrucciones SQL


    def cerrar(self):
        self.conexion.commit()  # Guardar los cambios realizados
        self.conexion.close()  # Cerrar la conexión a la base de datos

        
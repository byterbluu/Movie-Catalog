from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    

    #PRIMERO SE COLOCA NOMBRE DE LA TABLA Y ENTRE LOS PARENTESIS SE COLOCAN LOS VALORES DE LA TABLA 
    #VARCHAR SINGIFIA STRING Y LA CADENA DE CARECTERES

    sql = """           
    CREATE TABLE peliculas (
        id_pelicula INTEGER,
        nombre VARCHAR(100), 
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY (id_pelicula AUTOINCREMENT)
    )
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Tabla creada correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya existe'
        messagebox.showerror(titulo, mensaje)



def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'


    try:
        conexion.cursor.execute(sql)  #Ejecutar instruccion SQL
        conexion.cerrar() #Cerrar la conexión a la base de datos
        titulo = 'Borrar Registro'
        mensaje = 'Tabla Borrada correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No existe tabla para borrar'
        messagebox.showerror(titulo, mensaje)


class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero


    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion},  {self.genero}]'    
    

def guardar(pelicula):
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero) VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""    

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Guardar Registro'
        mensaje = 'Registro guardado correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Error al guardar'
        mensaje = 'La tabla pelicula no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)  


def listar():

    conexion = ConexionDB()

    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'     

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()  
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla pelicula no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)

    return lista_peliculas    


def editar(pelicula, id_pelicula):
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}' WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Editar Registro'
        mensaje = 'La tabla pelicula no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)  


def eliminar(id_pelicula):
    conexion = ConexionDB()

    sql = f"""DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Editar Registro'
        mensaje = 'No se pudo eliminar el registo'
        messagebox.showerror(titulo, mensaje) 

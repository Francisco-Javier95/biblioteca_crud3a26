# DAO: Data Acces Object
# libro_dao: Objeto de acceso a datos de la tabla de libro

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    # SELECT * FROM libro
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELCT * FROM libro")
        registros = cursor.fetchall()

        libros = []
        for registro in registros:
            libro = Libro(registro.libro_id, registro.libro_titulo, registro.libro_autor, registro.libro_isbn, registro.libro_disponible)
            libros.append(libro)

        cursor.close()
        conexion.close()
        return libros
# DAO: Data Acces Object
# libro_dao: Objeto de acceso a datos de la tabla de libro

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    # SELECT * FROM libro
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM libro")
        registros = cursor.fetchall()

        libros = []
        for registro in registros:
            libro = Libro (libro_id=registro[0], libro_titulo=registro[1], libro_autor=registro[2], libro_isbn=registro[3], libro_disponible=registro[4])
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros

    def insertar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            INSERT INTO libro (libro_titulo, libro_autor, libro_isbn, libro_disponible)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute8(
            sql, 
            (
                libro.libro_titulo,
                libro.libro_autor,
                libro.libro_isbn,
                libro.libro_disponible
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            UPDATE libro
            SET libro_titulo = %s, libro_autor = %s, libro_isbn = %s, libro_diseponible = %s
            WHERE libro_id = %s
        """

        cursor.execute8(
            sql, 
            (
                libro.libro_titulo,
                libro.libro_autor,
                libro.libro_isbn,
                libro.libro_disponible
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, libro_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM libro WHERE libro_id = %s",
            (libro_id,)
        )

        conexion.commit()
        cursor.close()
        conexion.close() 
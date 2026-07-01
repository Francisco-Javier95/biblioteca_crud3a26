# DAO: Data Acces Object
# usuario_dao: Objeto de acceso a datos de la tabla de usuario

from database.conexion import Conexion
from models.autor import Autor

class AutorDAO:

    # SELECT * FROM autor
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM autor")
        registros = cursor.fetchall()

        autores = []
        for registro in registros:
            autor = Autor (autor_id=registro[0], autor_nombre=registro[1])
            autores.append(autor)
        cursor.close()
        conexion.close()
        return autores

    def insertar(self, autor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            INSERT INTO autor (autor_nombre)
            VALUES (%s)
        """

        cursor.execute(
            sql, 
            (
                autor.autor_nombre,
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, autor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            UPDATE autor
            SET autor_nombre = %s
            WHERE autor_id = %s
        """

        cursor.execute(
            sql, 
            (
                autor.autor_nombre,
                autor.autor_id
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, autor_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM autor WHERE autor_id = %s",
            (autor_id.autor_id,)
        )

        conexion.commit()
        cursor.close()
        conexion.close() 
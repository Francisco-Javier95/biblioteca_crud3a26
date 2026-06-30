# DAO: Data Acces Object
# usuario_dao: Objeto de acceso a datos de la tabla de usuario

from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO:

    # SELECT * FROM usuario
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM usuario")
        registros = cursor.fetchall()

        usuarios = []
        for registro in registros:
            usuario = Usuario (usuario_id=registro[0], usuario_nombre=registro[1], usuario_matricula=registro[2], usuario_carrera=registro[3], usuario_email=registro[4])
            usuarios.append(usuario)
        cursor.close()
        conexion.close()
        return usuarios

    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            INSERT INTO usuario (usuario_nombre, usuario_matricula, usuario_carrera, usuario_email)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            sql, 
            (
                usuario.usuario_nombre,
                usuario.usuario_matricula,
                usuario.usuario_email,
                usuario.usuario_carrera                
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            UPDATE usuario
            SET usuario_nombre = %s, usuario_matricula = %s, usuario_carrera = %s, usuario_email = %s
            WHERE usuario_id = %s
        """

        cursor.execute(
            sql, 
            (
                usuario.usuario_nombre,
                usuario.usuario_matricula,
                usuario.usuario_email,
                usuario.usuario_carrera,
                usuario.usuario_id
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, usuario_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM usuario WHERE usuario_id = %s",
            (usuario_id.usuario_id,)
        )

        conexion.commit()
        cursor.close()
        conexion.close() 
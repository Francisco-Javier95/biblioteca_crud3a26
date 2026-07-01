from dao.libro_dao import LibroDAO
from dao.usuario_dao import UsuarioDAO
from dao.autor_dao import AutorDAO

from models.libro import Libro
from models.libro import Libro_eliminar
from models.usuario import Usuario
from models.usuario import Usuario_eliminar
from models.autor import Autor
from models.autor import Autor_eliminar

# ---------------------------------------CRUD LIBRO--------------------------------------------
def ver_libros():
    try:
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print("\n=== Libros en la biblioteca ===")

        if len(libros) == 0:
            print("Noy hay libros registrados.")
        else:
            for libro in libros:
                print("-----------------------------------------------------------------------------------------------------------------------------------------------")
                print(
                    f"ID: {libro.libro_id}, Título: {libro.libro_titulo}, "
                    f"Autor: {libro.libro_autor}, ISBN: {libro.libro_isbn}, "
                    f"Disponible: {'Sí' if libro.libro_disponible else 'NO'}"
                )

                print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_libro():
    libro_id = None
    libro_titulo = input("\nEscribe el titulo del libro: ")
    libro_autor = int(input("Escribe el nombre del autor: "))
    libro_isbn = input("Escriba el isbn del nuevo libro: ")
    libro_disponible = True

    try:
        libro_dao = LibroDAO()
        libro = Libro(libro_id, libro_titulo, libro_autor, libro_isbn, libro_disponible)
        libro_dao.insertar(libro)
        print("Insercion realizada con éxito")
    except Exception as e:
        print("Error al insertar un libro nuevo")
        print(e)

def actualizar_libro():
    print("Selecciona el libro a actualizar")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        libro_id = int(input("\nEscribe el id del libro a actualizar: "))

        libro_titulo = input("Escribe el nuevo titulo: ")
        libro_autor = input("Escribe el nuevo autor: ")
        libro_isbn = input("Escribe el nuevo ISBN: ")
        libro_disponible = bool(input("Escribe el nuevo valor de disponible: "))

        libro = Libro(libro_id, libro_titulo, libro_autor, libro_isbn, libro_disponible)
        libro_dao.actualizar(libro)
        print(f"El libro {libro_id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar un libro")
        print (e)

def eliminar_libro():
    try:
        ver_libros() # mostrar todos los registros de libros

        libro_id = int(input("\nEscribe el ID del libro a eliminar: "))

        libro_dao = LibroDAO()
        libro = Libro_eliminar(libro_id)
        libro_dao.eliminar(libro)

        print(f"Libro {libro_id} eliminado exitosamente")

    except Exception as e:
        print("Error al eliminar el libro")
        print(e)
    
# ---------------------------------------FIN CRUD LIBRO-----------------------------------------

# ---------------------------------------CRUD USUARIO-------------------------------------------
def ver_usuario():
    try:
        usuario_dao = UsuarioDAO()

        usuarios = usuario_dao.obtener_todos()

        print("\n=== Usuarios registrados en la biblioteca ===")

        if len(usuarios) == 0:
            print("Noy hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print("-----------------------------------------------------------------------------------------------------------------------------------------------")
                print(
                    f"ID: {usuario.usuario_id}, Nombre: {usuario.usuario_nombre}, "
                    f"Matrícula: {usuario.usuario_matricula}, Carrera: {usuario.usuario_carrera}, "
                    f"Email: {usuario.usuario_email}"
                )

                print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nConexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def registrar_usuario():
    usuario_id = None
    usuario_nombre = input("\nEscribe nombre del usuario: ")
    usuario_matricula = input("Escribe la matricula: ")
    usuario_carrera = int(input("Escribe la carrera: "))
    usuario_email = input("Escribe el correo electrónico: ")

    try:
        usuario_dao = UsuarioDAO()
        usuario = Usuario(usuario_id, usuario_nombre, usuario_matricula, usuario_carrera, usuario_email)
        usuario_dao.insertar(usuario)
        print("Insercion realizada con éxito")
    except Exception as e:
        print("Error al insertar un libro nuevo")
        print(e)

def actualizar_usuario():
    print("Selecciona el usuario a actualizar")
    try:
        ver_usuario()
        usuario_id = int(input("\nEscribe el id del usuario a actualizar: "))

        usuario_nombre = input("Escribe el nuevo nombre: ")
        usuario_matricula = input("Escribe la nueva matrícula: ")
        usuario_carrera = int(input("Escriba la nueva carrera: "))
        usuario_email = input("Escribe el nuevo correo electrónico: ")

        usuario_dao = UsuarioDAO()
        usuario = Usuario(usuario_id, usuario_nombre, usuario_matricula, usuario_carrera, usuario_email)
        usuario_dao.actualizar(usuario)

        print(f"El usuario {usuario_id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar el usuario")
        print (e)

def eliminar_usuario():
    try:
        ver_usuario() # mostrar todos los registros de usuario

        usuario_id = int(input("\n" \
        "" \
        "" \
        "Escribe el ID del usuario a eliminar: "))

        usuario_dao = UsuarioDAO()
        usuario = Usuario_eliminar(usuario_id)
        usuario_dao.eliminar(usuario)

        print(f"Usuario {usuario_id} eliminado exitosamente")

    except Exception as e:
        print("Error al eliminar el usuario")
        print(e)
    
# ---------------------------------------FIN CRUD USUARIO-----------------------------------------

# ---------------------------------------CRUD AUTOR-------------------------------------------
def ver_autor():
    try:
        autor_dao = AutorDAO()

        autores = autor_dao.obtener_todos()

        print("\n=== Autores registrados en la biblioteca ===")

        if len(autores) == 0:
            print("Noy hay autores registrados.")
        else:
            for autor in autores:
                print("-----------------------------------------------------------------------------------------------------------------------------------------------")
                print(
                    f"ID: {autor.autor_id}, Nombre: {autor.autor_nombre}"
                )

                print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nConexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def registrar_autor():
    autor_id = None
    autor_nombre = input("\nEscribe nombre del autor: ")

    try:
        autor_dao = AutorDAO()
        autor = Autor(autor_id, autor_nombre)
        autor_dao.insertar(autor)
        print("Insercion realizada con éxito")
    except Exception as e:
        print("Error al insertar un autor nuevo")
        print(e)

def actualizar_autor():
    print("Selecciona el autor a actualizar")
    try:
        ver_autor()
        autor_id = int(input("\nEscribe el ID del autor a actualizar: "))

        autor_nombre = input("Escribe el nuevo nombre: ")

        autor_dao = AutorDAO()
        autor = Autor(autor_id, autor_nombre)
        autor_dao.actualizar(autor)

        print(f"El autor {autor_id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar el autor")
        print (e)

def eliminar_autor():
    try:
        ver_autor() # mostrar todos los registros de autor

        autor_id = int(input("\n" \
        "" \
        "" \
        "Escribe el ID del autor a eliminar: "))

        autor_dao = AutorDAO()
        autor = Autor_eliminar(autor_id)
        autor_dao.eliminar(autor)

        print(f"Autor {autor_id} eliminado exitosamente")

    except Exception as e:
        print("Error al eliminar el autor")
        print(e)
    
# ---------------------------------------FIN CRUD AUTOR-----------------------------------------

def menu_libro():
    print("\nMenú de opciones LIBRO")
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro disponible")
    print("3. Actualizar un libro disponible")
    print("4. Eliminar un libro disponible")
    opcion = int(input("Selecciona una opcion (1-4): "))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()

def menu_usuario():
    print("\nMenú de opciones USUARIO")
    print("1. Ver todos los usuario")
    print("2. Registrar nuevo usuario")
    print("3. Actualizar un usuario")
    print("4. Eliminar un usuario")
    opcion = int(input("Selecciona una opcion (1-4): "))

    match opcion:
        case 1:
            ver_usuario()
        case 2:
            registrar_usuario()
        case 3:
            actualizar_usuario()
        case 4:
            eliminar_usuario()

def menu_autor():
    print("\nMenú de opciones AUTOR")
    print("1. Ver todos los autores")
    print("2. Registrar nuevo autor")
    print("3. Actualizar un autor")
    print("4. Eliminar un autor")
    opcion = int(input("Selecciona una opcion (1-4): "))

    match opcion:
        case 1:
            ver_autor()
        case 2:
            registrar_autor()
        case 3:
            actualizar_autor()
        case 4:
            eliminar_autor()

def main():
    print("\n===== BIBLIOTECA UNIVERSITARIA =====")
    print("Menú de opciones: ")
    print("1. Gestión de libros")
    print("2. Gestión de usuarios")
    print("3. Gestión de autores")
    opcion = int(input("Selecciona una opción (1-3): "))
    match opcion:
        case 1: menu_libro()
        case 2: menu_usuario()
        case 3: menu_autor()
        
    print("Gracias por usar la aplicación de biblioteca universitaria :)")


if __name__ == "__main__":
    main()
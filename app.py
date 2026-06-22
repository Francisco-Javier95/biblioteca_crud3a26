from dao.libro_dao import LibroDAO
from models.libro import Libro

def ver_libros():
    try:
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print("=== Libros en la biblioteca ===")

        if len(libros) == 0:
            print("Noy hay libros registrados.")
        else:
            for libro in libros:
                print("-------------------------------------")
                print(
                    f"ID: {libro.libro_id}, Título: {libro.libro_titulo}, "
                    f"Autor: {libro.libro_autor}, ISBN: {libro.libro_isbn}, "
                    f"Disponible: {'Sí' if libro.libro_disponible else 'NO'}"
                )

                print("-------------------------------------")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_libro():
    libro_titulo = input("Escribe el titulo del libro: ")
    libro_autor = int(input("Escribe el nombre del autor: "))
    libro_isbn = input("Escriba el isbn del nuevo libro: ")
    libro_disponible = True

    try:
        libro_dao = LibroDAO()
        id = LibroDAO.obtener_ultimo_id() + 1
        libro = Libro(id, libro_titulo, libro_autor, libro_isbn, libro_disponible)
        libro_dao.insertar(libro)
        print("Insercion realizada con éxito")
    except Exception as e:
        print("Error al insertar un libro nuevo")
        print(e)

def main():
    print("=== BIBLIOTECA UNIVERSITARIA ===")
    print("Menu de opciones")
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

if __name__ == "__main__":
    main()
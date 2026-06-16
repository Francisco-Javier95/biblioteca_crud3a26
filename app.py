from dao.libro_dao import LibroDAO
from models.libro import Libro

def main():
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
                    f"Disponible: {'Sí' if libro.libro_diponible else 'NO'}"
                )

                print("-------------------------------------")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

if __name__ == "__main__":
    main()
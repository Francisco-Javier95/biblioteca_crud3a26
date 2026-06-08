class Libro:

    # Constructor
    def __init__(self, id_libro, titulo, autor, isbn):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True # Por defecto, el libro está disponible

    def prestar(self):
        if self.diponible:
            self.disponible = False
            return True
        return False
    
    def devolver(self):
        self.disponible = True

    def mostrar_info(self):
        return f"Libro ID: {self.id_libro}, Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {'Sí' if self.disponible else 'No'} "


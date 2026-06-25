class Libro:

    # Constructor
    def __init__(self, libro_id, libro_titulo, libro_autor, libro_isbn, libro_disponible):
        self.libro_id = libro_id
        self.libro_titulo = libro_titulo
        self.libro_autor = libro_autor
        self.libro_isbn = libro_isbn
        self.libro_disponible = libro_disponible # Por defecto, el libro está disponible

    def prestar(self):
        if self.diponible:
            self.disponible = False
            return True
        return False
    
    def devolver(self):
        self.disponible = True

    def mostrar_info(self):
        return f"Libro ID: {self.libro_id}, Título: {self.libro_titulo}, Autor: {self.libro_autor}, ISBN: {self.libro_isbn}, Disponible: {'Sí' if self.libro_disponible else 'No'} "
    



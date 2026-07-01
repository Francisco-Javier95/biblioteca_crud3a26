class Autor:

    # constructor
    def __init__(self, autor_id, autor_nombre):
        self.autor_id = autor_id
        self.autor_nombre = autor_nombre

    def mostrar_info(self):
        return f"Autor ID: {self.autor_id}, Nombre: {self.autor_nombre}"
    
class Autor_eliminar:

    # constructor
    def __init__(self, autor_id):
        self.autor_id = autor_id

from models.libro import Libro

class Prestamo:

    # Contructor
    def __init__(self, id_prestamo, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False # Valor por defecto, el préstamo no ha sido devuelto

    def registrar_devolucion(self):
        self.devuelto = True
        self.libro.devolver() # Marca el libro como disponible nuevamente

    def mostrar_info(self):
        return f"Prestamo ID: {self.id_prestamo}, Usuario: {self.usuario}, Libro: {self.libro}, Fecha de Préstamo: {self.fecha_prestamo}, Fecha de Devolución: {self.fecha_devolucion}, Devuelto: {'Sí' if self.devuelto else 'No'}"

    